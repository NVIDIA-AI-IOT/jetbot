try:
    DEFAULT_CAMERA = os.environ['JETBOT_DEFAULT_CAMERA']
except:
    DEFAULT_CAMERA = 'opencv_gst_camera'


if DEFAULT_CAMERA == 'zmq_camera':
    from .zmq_camera import ZmqCamera
    Camera = ZmqCamera
else:
    from .opencv_gst_camera import OpenCvGstCamera
    Camera = OpenCvGstCamera