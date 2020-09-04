import traitlets
import os

    
class Camera(traitlets.HasTraits):
    
    value = traitlets.Any()
    
    @staticmethod
    def default_camera_class():
        try:
            default = os.environ['JETBOT_DEFAULT_CAMERA']
        except:
            default = 'opencv_gst_camera'
            
        if default == 'zmq_camera':
            from .zmq_camera import ZmqCamera
            return ZmqCamera
        else:
            from .opencv_gst_camera import OpenCvGstCamera
            return OpenCvGstCamera
    
    @staticmethod
    def instance(*args, **kwargs):
        return Camera.default_camera_class()(*args, **kwargs)
    
    def widget(self):
        if hasattr(self, '_widget'):
            return self._widget   # cache widget, so we don't duplicate links
        from ipywidgets import Image
        from jetbot.image import bgr8_to_jpeg
        image = Image()
        traitlets.dlink((self, 'value'), (image, 'value'), transform=bgr8_to_jpeg)
        self._widget = image
        return image