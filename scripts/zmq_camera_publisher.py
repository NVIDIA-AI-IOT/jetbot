import argparse
import signal
import zmq
import time
import numpy as np
import gi
gi.require_version('Gst', '1.0')
import logging
import atexit
import numpy as np
from gi.repository import GObject, Gst


Gst.init(None)


class GstCamera(object):
    
    def __init__(self, sensor_mode=0, width=224, height=224, fps=21, capture_width=816, capture_height=616):
        
        self.mainloop = GObject.MainLoop()
        
        print(sensor_mode)
        GST_STRING = 'nvarguscamerasrc sensor-mode={sensor_mode} '\
            '! video/x-raw(memory:NVMM), width={capture_width}, height={capture_height}, format=(string)NV12, framerate=(fraction){fps}/1 !'\
            ' nvvidconv '\
            '! video/x-raw, width=(int){width}, height=(int){height}, format=(string)BGRx !'\
            ' videoconvert '\
            '! video/x-raw, format=(string)BGR !'\
            ' appsink name=sink'.format(
            sensor_mode=sensor_mode,
            width=width, 
            height=height, 
            fps=fps, 
            capture_width=capture_width,
            capture_height=capture_height
        )
        print(GST_STRING)
        
        self.pipeline = Gst.parse_launch(GST_STRING)
        
        appsink = self.pipeline.get_by_name('sink')

        appsink.set_property('emit-signals', True)
        appsink.set_property('max-buffers', 1)
        appsink.connect('new-sample', self._on_new_sample)
        
        
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message::eos", self._on_eos)
        self.bus.connect("message::error", self._on_error)
        
        self._on_image_callbacks = set()
        
        atexit.register(self.stop)
        
    
    def __del__(self):
        self.stop()
        
    def on_image(self, callback):
        self._on_image_callbacks.add(callback)
        
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
        
        for cb in self._on_image_callbacks:
            cb(image)
            
        buf.unmap(mapinfo)
        
        return Gst.FlowReturn.OK
    
    def start(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        self.mainloop.run()
        
    def stop(self):
        self.pipeline.set_state(Gst.State.NULL)
        self.mainloop.quit()
        
    def _on_eos(self, bus, msg):
        self.stop()
    
    def _on_error(self, bus, msg):
        self.stop()
        
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=1807)
    parser.add_argument('--sensor_mode', type=int, default=0)
    parser.add_argument('--width', type=int, default=224)
    parser.add_argument('--height', type=int, default=224)
    parser.add_argument('--fps', type=int, default=21)
    parser.add_argument('--capture_width', type=int, default=816)
    parser.add_argument('--capture_height', type=int, default=616)
    args = parser.parse_args()
    
        
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
#     socket.setsockopt(zmq.CONFLATE, 1)  # latest 1 message
    socket.bind("tcp://*:%d" % args.port)

    camera = GstCamera(
        sensor_mode=args.sensor_mode,
        width=args.width,
        height=args.height,
        fps=args.fps,
        capture_width=args.capture_width,
        capture_height=args.capture_height
    )
    
    def publish_image(image):
        global socket, args
        socket.send(image)
        
    camera.on_image(publish_image)
    
    print("starting camera")
    
    def shutdown(*args, **kwargs):
        global camera
        camera.stop()
        
    signal.signal(signal.SIGTERM, shutdown)  # shutdown gracefully
    
    try:
        camera.start()  # will run until EOS / error on GST bus
    except KeyboardInterrupt:
        shutdown()