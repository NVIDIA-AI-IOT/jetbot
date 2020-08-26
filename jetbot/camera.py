import traitlets
import gi
gi.require_version('Gst', '1.0')
import logging
import atexit
import numpy as np
from gi.repository import GObject, Gst


Gst.init(None)


class Camera(traitlets.HasTraits):
    
    value = traitlets.Any()
    
    def __init__(self, width=224, height=224, fps=21, capture_width=816, capture_height=616):
        
        GST_STRING = 'nvarguscamerasrc' + \
            '! video/x-raw(memory:NVMM), width={capture_width}, height={capture_height}, format=(string)NV12, framerate=(fraction){fps}/1 !'\
            ' nvvidconv '\
            '! video/x-raw, width=(int){width}, height=(int){height}, format=(string)BGRx !'\
            ' videoconvert '\
            '! video/x-raw, format=(string)BGR !'\
            ' appsink name=sink'.format(
            width=width, 
            height=height, 
            fps=fps, 
            capture_width=capture_width,
            capture_height=capture_height
        )
        
        self.pipeline = Gst.parse_launch(GST_STRING)
        
        appsink = self.pipeline.get_by_name('sink')

        appsink.set_property('emit-signals', True)
        appsink.set_property('max-buffers', 1)
        appsink.connect('new-sample', self._on_new_sample)
        
        
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message::eos", self._on_eos)
        self.bus.connect("message::error", self._on_error)
        
        self.start()
        
        atexit.register(self.stop)
    
    def __del__(self):
        self.stop()
        
    def _on_new_sample(self, appsink):
        sample = appsink.emit('pull-sample')
        buf = sample.get_buffer()
        caps = sample.get_caps()
        height = caps.get_structure(0).get_value('height')
        width = caps.get_structure(0).get_value('width')
        (result, mapinfo) = buf.map(Gst.MapFlags.READ)

        image = np.ndarray(
            shape=(height, width, 3),
            buffer=buf.extract_dup(0, buf.get_size()),  # extract_dup to copy
            dtype=np.uint8
        )
        
        self.value = image
            
        buf.unmap(mapinfo)
        
        return Gst.FlowReturn.OK
    
    def start(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        
    def stop(self):
        self.pipeline.set_state(Gst.State.NULL)
        
    def _on_eos(self, bus, msg):
        self.stop()
    
    def _on_error(self, bus, msg):
        self.stop()
    
    @staticmethod
    def instance(*args, **kwargs):
        return Camera(*args, **kwargs)