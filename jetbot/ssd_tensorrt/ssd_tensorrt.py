import ctypes
import graphsurgeon as gs
import numpy as np
import os
import subprocess
import tensorrt as trt
import uff

TRT_INPUT_NAME = 'input'
TRT_OUTPUT_NAME = 'nms'
FROZEN_GRAPH_NAME = 'frozen_inference_graph.pb'
LABEL_IDX = 1
CONFIDENCE_IDX = 2
X0_IDX = 3
Y0_IDX = 4
X1_IDX = 5
Y1_IDX = 6


def parse_boxes(outputs):
    bboxes = outputs[0]
            
    # iterate through each image index
    all_detections = []
    for i in range(bboxes.shape[0]):

        detections = []
        # iterate through each bounding box
        for j in range(bboxes.shape[2]):

            bbox = bboxes[i][0][j]
            label = bbox[LABEL_IDX]

            # last detection if < 0
            if label < 0: 
                break

            detections.append(dict(
                label=int(label),
                confidence=float(bbox[CONFIDENCE_IDX]),
                bbox=[
                    float(bbox[X0_IDX]),
                    float(bbox[Y0_IDX]),
                    float(bbox[X1_IDX]),
                    float(bbox[Y1_IDX])
                ]
            ))

        all_detections.append(detections)

    return all_detections


def load_plugins():
    library_path = os.path.join(
        os.path.dirname(__file__), 'libssd_tensorrt.so')
    ctypes.CDLL(library_path)


def _get_feature_map_shape(config):
    width = config.model.ssd.image_resizer.fixed_shape_resizer.width
    fms = []
    curr = int(np.ceil(width / 16.0))
    for i in range(6):
        fms.append(curr)
        curr = int(np.ceil(curr / 2.0))
    return fms


def _load_config(config_path):
    from object_detection.protos.pipeline_pb2 import TrainEvalPipelineConfig
    from google.protobuf.text_format import Merge
    config = TrainEvalPipelineConfig()

    with open(config_path, 'r') as f:
        config_str = f.read()

    lines = config_str.split('\n')
    lines = [line for line in lines if 'batch_norm_trainable' not in line]
    config_str = '\n'.join(lines)

    Merge(config_str, config)

    return config


def ssd_pipeline_to_uff(checkpoint_path, config_path,
                        tmp_dir='exported_model'):

    from object_detection import exporter
    import tensorflow as tf

    # TODO(@jwelsh): Implement by extending model builders with
    # TensorRT plugin stubs.  Currently, this method uses pattern
    # matching which is a bit hacky and subject to fail when TF
    # object detection API exporter changes.  We should add object
    # detection as submodule to avoid versioning incompatibilities.

    config = _load_config(config_path)
    frozen_graph_path = os.path.join(tmp_dir, FROZEN_GRAPH_NAME)

    # get input shape
    channels = 3
    height = config.model.ssd.image_resizer.fixed_shape_resizer.height
    width = config.model.ssd.image_resizer.fixed_shape_resizer.width

    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = True

    # export checkpoint and config to frozen graph
    with tf.Session(config=tf_config) as tf_sess:
        with tf.Graph().as_default() as tf_graph:
            subprocess.call(['mkdir', '-p', tmp_dir])
            exporter.export_inference_graph(
                'image_tensor',
                config,
                checkpoint_path,
                tmp_dir,
                input_shape=[1, None, None, 3])

    dynamic_graph = gs.DynamicGraph(frozen_graph_path)

    # remove all assert nodes
    #all_assert_nodes = dynamic_graph.find_nodes_by_op("Assert")
    #dynamic_graph.remove(all_assert_nodes, remove_exclusive_dependencies=True)

    # forward all identity nodes
    all_identity_nodes = dynamic_graph.find_nodes_by_op("Identity")
    dynamic_graph.forward_inputs(all_identity_nodes)

    # create input plugin
    input_plugin = gs.create_plugin_node(
        name=TRT_INPUT_NAME,
        op="Placeholder",
        dtype=tf.float32,
        shape=[1, height, width, channels])

    # create anchor box generator
    anchor_generator_config = config.model.ssd.anchor_generator.ssd_anchor_generator
    box_coder_config = config.model.ssd.box_coder.faster_rcnn_box_coder
    priorbox_plugin = gs.create_plugin_node(
        name="priorbox",
        op="GridAnchor_TRT",
        minSize=anchor_generator_config.min_scale,
        maxSize=anchor_generator_config.max_scale,
        aspectRatios=list(anchor_generator_config.aspect_ratios),
        variance=[
            1.0 / box_coder_config.y_scale, 1.0 / box_coder_config.x_scale,
            1.0 / box_coder_config.height_scale,
            1.0 / box_coder_config.width_scale
        ],
        featureMapShapes=_get_feature_map_shape(config),
        numLayers=config.model.ssd.anchor_generator.ssd_anchor_generator.
        num_layers)

    # create nms plugin
    nms_config = config.model.ssd.post_processing.batch_non_max_suppression
    nms_plugin = gs.create_plugin_node(
        name=TRT_OUTPUT_NAME,
        op="NMS_TRT",
        shareLocation=1,
        varianceEncodedInTarget=0,
        backgroundLabelId=0,
        confidenceThreshold=nms_config.score_threshold,
        nmsThreshold=nms_config.iou_threshold,
        topK=nms_config.max_detections_per_class,
        keepTopK=nms_config.max_total_detections,
        numClasses=config.model.ssd.num_classes + 1,  # add background
        inputOrder=[1, 2, 0],
        confSigmoid=1,
        isNormalized=1,
        scoreConverter="SIGMOID",
        codeType=3)

    priorbox_concat_plugin = gs.create_node(
        "priorbox_concat", op="ConcatV2", dtype=tf.float32, axis=2)

    boxloc_concat_plugin = gs.create_plugin_node(
        "boxloc_concat",
        op="FlattenConcat_TRT",
        dtype=tf.float32,
    )

    boxconf_concat_plugin = gs.create_plugin_node(
        "boxconf_concat",
        op="FlattenConcat_TRT",
        dtype=tf.float32,
    )

    namespace_plugin_map = {
        "MultipleGridAnchorGenerator": priorbox_plugin,
        "Postprocessor": nms_plugin,
        "Preprocessor": input_plugin,
        "ToFloat": input_plugin,
        "image_tensor": input_plugin,
        "Concatenate": priorbox_concat_plugin,
        "concat": boxloc_concat_plugin,
        "concat_1": boxconf_concat_plugin
    }

    dynamic_graph.collapse_namespaces(namespace_plugin_map)

    # fix name
    for i, name in enumerate(
            dynamic_graph.find_nodes_by_op('NMS_TRT')[0].input):
        if TRT_INPUT_NAME in name:
            dynamic_graph.find_nodes_by_op('NMS_TRT')[0].input.pop(i)

    dynamic_graph.remove(
        dynamic_graph.graph_outputs, remove_exclusive_dependencies=False)

    uff_buffer = uff.from_tensorflow(dynamic_graph.as_graph_def(),
                                     [TRT_OUTPUT_NAME])

    return uff_buffer


def ssd_uff_to_engine(uff_buffer,
                      fp16_mode=True,
                      max_batch_size=1,
                      max_workspace_size=1 << 26,
                      min_find_iterations=2,
                      average_find_iterations=1,
                      strict_type_constraints=False,
                      log_level=trt.Logger.INFO):

    # create the tensorrt engine
    with trt.Logger(log_level) as logger, trt.Builder(logger) as builder, \
        builder.create_network() as network, trt.UffParser() as parser:

        # init built in plugins
        trt.init_libnvinfer_plugins(logger, '')

        # load jetbot plugins
        load_plugins()

        meta_graph = uff.model.uff_pb2.MetaGraph()
        meta_graph.ParseFromString(uff_buffer)

        input_node = None
        for n in meta_graph.ListFields()[3][1][0].nodes:
            if 'Input' in n.operation:
                input_node = n

        channels = input_node.fields['shape'].i_list.val[3]
        height = input_node.fields['shape'].i_list.val[1]
        width = input_node.fields['shape'].i_list.val[2]

        # parse uff to create network
        parser.register_input(TRT_INPUT_NAME, (channels, height, width))
        parser.register_output(TRT_OUTPUT_NAME)
        parser.parse_buffer(uff_buffer, network)

        builder.fp16_mode = fp16_mode
        builder.max_batch_size = max_batch_size
        builder.max_workspace_size = max_workspace_size
        builder.min_find_iterations = min_find_iterations
        builder.average_find_iterations = average_find_iterations
        builder.strict_type_constraints = strict_type_constraints

        engine = builder.build_cuda_engine(network)

    return engine
