import traitlets
import gi
gi.require_version('Gst', '1.0')
import logging
import atexit
import numpy as np
import time
from gi.repository import GObject, Gst


Gst.init(None)


class JpegEncoder(object):
    
    def __init__(self, width=224, height=224, fps=21):
        
        
        CAPS = "video/x-raw,format=BGR,width={width},height={height},framerate={fps}/1".format(
            width=width,
            height=height,
            fps=fps
        )
        
        GST_STRING = 'appsrc name=src emit-signals=True is-live=True caps=video/x-raw,format=BGR,width={width},height={height},framerate={fps}/1 !'\
            ' nvjpegenc '\
            '! image/jpeg,width={width},height={height},framerate={fps}/1 !'\
            ' appsink name=sink'.format(
            width=width,
            height=height,
            fps=fps
        )
        
        self.pipeline = Gst.parse_launch(GST_STRING)
        self.appsrc = self.pipeline.get_by_name('src')
        
        appsink = self.pipeline.get_by_name('sink')
        
        self.appsrc.set_property("format", Gst.Format.TIME)
        self.appsrc.set_property("block", True)  # block push-buffers when queue is full
        
        appsink.set_property('max-buffers', 1)
        self.appsink = appsink
        
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message::eos", self._on_eos)
        self.bus.connect("message::error", self._on_error)
        
        self.start()
        
        atexit.register(self.stop)
    
    def __del__(self):
        self.stop()
        
    def start(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        
    def stop(self):
        #TODO(jwelsh): do we need to handle EOS?
        self.pipeline.set_state(Gst.State.NULL)
        
    def _on_eos(self, bus, msg):
        self.stop()
    
    def _on_error(self, bus, msg):
        self.stop()
        
    def encode(self, image):
        buffer = Gst.Buffer.new_wrapped(image.tobytes())
        self.appsrc.emit("push-buffer", buffer)
        sample = self.appsink.emit('pull-sample')  # blocks until sample avaialable
        buf = sample.get_buffer()
        (result, mapinfo) = buf.map(Gst.MapFlags.READ)
        return buf.extract_dup(0, buf.get_size())