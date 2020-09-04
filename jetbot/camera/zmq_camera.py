import threading
import traitlets
import sys
import zmq
import numpy as np
import atexit
from .camera_base import CameraBase


def recv_image(socket, dtype, shape):
    data = socket.recv()
    buf = memoryview(data)
    array = np.frombuffer(buf, dtype=dtype)
    return array.reshape(shape)

    
class ZmqCamera(CameraBase):
    
    value = traitlets.Any(value=np.zeros((224, 224, 3), dtype=np.uint8), default_value=np.zeros((224, 224, 3), dtype=np.uint8))
    
    def __init__(self, *args, **kwargs):
        self.value = np.zeros((224, 224, 3), dtype=np.uint8)  # set default image
        super().__init__(self, *args, **kwargs)
        
        self._running = False
        self._port = 1807
        self._image_shape = (224, 224, 3)
        self._image_dtype = np.uint8
        self.start()
        atexit.register(self.stop)
        
    def __del__(self):
        self.stop()
        
    def _run(self):
        
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.CONFLATE, 1)  # last msg only.
        self.socket.setsockopt(zmq.SUBSCRIBE, b'') # all topics
        self.socket.connect("tcp://localhost:%d" % self._port)
        
        while self._running:
            image = recv_image(self.socket, self._image_dtype, self._image_shape)
            self.value = image
            
        self.socket.close()
            
    def start(self):
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._run)
        self._thread.start()
        
    def stop(self):
        if not self._running:
            return
        self._running = False
        self._thread.join()
        
    @staticmethod
    def instance(*args, **kwargs):
        return ZmqCamera(*args, **kwargs)