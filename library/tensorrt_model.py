import torch
import tensorrt as trt
import atexit


def torch_dtype_to_trt(dtype):
    if dtype == torch.int8:
        return trt.int8
    elif dtype == torch.int32:
        return trt.int32
    elif dtype == torch.float16:
        return trt.float16
    elif dtype == torch.float32:
        return trt.float32
    else:
        raise TypeError('%s is not supported by tensorrt' % dtype)


def torch_dtype_from_trt(dtype):
    if dtype == trt.int8:
        return torch.int8
    elif dtype == trt.int32:
        return torch.int32
    elif dtype == trt.float16:
        return torch.float16
    elif dtype == trt.float32:
        return torch.float32
    else:
        raise TypeError('%s is not supported by torch' % dtype)


def torch_device_to_trt(device):
    if device.type == torch.device('cuda').type:
        return trt.TensorLocation.DEVICE
    elif device.type == torch.device('cpu').type:
        return trt.TensorLocation.HOST
    else:
        return TypeError('%s is not supported by tensorrt' % device)


def torch_device_from_trt(device):
    if device == trt.TensorLocation.DEVICE:
        return torch.device('cuda')
    elif device == trt.TensorLocation.HOST:
        return torch.device('cpu')
    else:
        return TypeError('%s is not supported by torch' % device)

    
class TRTModel(object):
    
    def __init__(self, engine_path, input_names=None, output_names=None, final_shapes=None):
        
        # load engine
        self.logger = trt.Logger()
        self.runtime = trt.Runtime(self.logger)
        with open(engine_path, 'rb') as f:
            self.engine = self.runtime.deserialize_cuda_engine(f.read())
        self.context = self.engine.create_execution_context()
        
        if input_names is None:
            self.input_names = self._trt_input_names()
        else:
            self.input_names = input_names
            
        if output_names is None:
            self.output_names = self._trt_output_names()
        else:
            self.output_names = output_names
            
        self.final_shapes = final_shapes
        
        # destroy at exit
        atexit.register(self.destroy)
    
    def _input_binding_indices(self):
        return [i for i in range(self.engine.num_bindings) if self.engine.binding_is_input(i)]
    
    def _output_binding_indices(self):
        return [i for i in range(self.engine.num_bindings) if not self.engine.binding_is_input(i)]
    
    def _trt_input_names(self):
        return [self.engine.get_binding_name(i) for i in self._input_binding_indices()]
    
    def _trt_output_names(self):
        return [self.engine.get_binding_name(i) for i in self._output_binding_indices()]
    
    def create_output_buffers(self, batch_size):
        outputs = [None] * len(self.output_names)
        for i, output_name in enumerate(self.output_names):
            idx = self.engine.get_binding_index(output_name)
            dtype = torch_dtype_from_trt(self.engine.get_binding_dtype(idx))
            if self.final_shapes is not None:
                shape = (batch_size, ) + self.final_shapes[i]
            else:
                shape = (batch_size, ) + tuple(self.engine.get_binding_shape(idx))
            device = torch_device_from_trt(self.engine.get_location(idx))
            output = torch.empty(size=shape, dtype=dtype, device=device)
            outputs[i] = output
        return outputs
    
    def execute(self, *inputs):
        batch_size = inputs[0].shape[0]
        
        bindings = [None] * (len(self.input_names) + len(self.output_names))
        
        # map input bindings
        inputs_torch = [None] * len(self.input_names)
        for i, name in enumerate(self.input_names):
            idx = self.engine.get_binding_index(name)
            
            # convert to appropriate format
            inputs_torch[i] = torch.from_numpy(inputs[i])
            inputs_torch[i] = inputs_torch[i].to(torch_device_from_trt(self.engine.get_location(idx)))
            inputs_torch[i] = inputs_torch[i].type(torch_dtype_from_trt(self.engine.get_binding_dtype(idx)))
            
            bindings[idx] = int(inputs_torch[i].data_ptr())
            
        output_buffers = self.create_output_buffers(batch_size)
        
        # map output bindings
        for i, name in enumerate(self.output_names):
            idx = self.engine.get_binding_index(name)
            bindings[idx] = int(output_buffers[i].data_ptr())
        
        self.context.execute(batch_size, bindings)
        
        outputs = [buffer.cpu().numpy() for buffer in output_buffers]
                                 
        return outputs
    
    def __call__(self, *inputs):
        return self.execute(*inputs)

    def destroy(self):
        self.runtime.destroy()
        self.logger.destroy()
        self.engine.destroy()
        self.context.destroy()