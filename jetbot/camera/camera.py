import traitlets


    
class Camera(traitlets.HasTraits):
    
    value = traitlets.Any()
    
    DEFAULT_CAMERA_CLASS = 'OpenCvGstCamera'
    
    @staticmethod
    def default_camera_class():
        from .opencv_gst_camera import OpenCvGstCamera
        return OpenCvGstCamera
    
    @staticmethod
    def instance(*args, **kwargs):
        return Camera.default_camera_class()(*args, **kwargs)