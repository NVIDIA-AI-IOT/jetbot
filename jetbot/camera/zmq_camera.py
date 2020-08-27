import threading
import traitlets
import sys
import zmq
import numpy as np
import atexit
from .camera import Camera


def recv_topic_numpy(socket):
    
    topic, dtype, shape, data = socket.recv_multipart(copy=True)
    import pdb
    shape = tuple([int(s) for s in bytes(shape).decode('utf-8').split(',')])
    buf = memoryview(data)
    array = np.frombuffer(buf, dtype=bytes(dtype).decode('utf-8'))
    return bytes(topic).decode('utf-8'), array.reshape(shape)


class ZmqCamera(Camera):
    
    value = traitlets.Any(value=np.zeros((224, 224, 3), dtype=np.uint8), default_value=np.zeros((224, 224, 3), dtype=np.uint8))
    
    def __init__(self, *args, **kwargs):
        
#         self.value = np.zeros((224, 224, 3), dtype=np.uint8)  # set default image
        self._running = False
        self._port = 1807
        self._topic = "image"
        self.start()
        atexit.register(self.stop)
        
    def __del__(self):
        self.stop()
        
    def _run(self):
        
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self._topic)
        self.socket.connect("tcp://localhost:%d" % self._port)
        
        while self._running:
            topic, image = recv_topic_numpy(self.socket)
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