import traitlets
import os

    
class CameraBase(traitlets.HasTraits):
    
    value = traitlets.Any()
    
    @staticmethod
    def instance(*args, **kwargs):
        raise NotImplementedError
    
    def widget(self):
        if hasattr(self, '_widget'):
            return self._widget   # cache widget, so we don't duplicate links
        from ipywidgets import Image
        from jetbot.image import bgr8_to_jpeg
        image = Image()
        traitlets.dlink((self, 'value'), (image, 'value'), transform=bgr8_to_jpeg)
        self._widget = image
        return image
    
