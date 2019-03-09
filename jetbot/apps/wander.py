import argparse
import traitlets
from jetbot import Robot
from jetbot import Camera
import torch
import torchvision
import torch.nn.functional as F
import time
import cv2
import numpy as np
import signal


class WanderApplication(traitlets.HasTraits):
    
    collision_model = traitlets.Unicode()
    
    def __init__(self, *args, **kwargs):
        super(WanderApplication, self).__init__(*args, **kwargs)
        self.mean = 255.0 * np.array([0.485, 0.456, 0.406])
        self.stdev = 255.0 * np.array([0.229, 0.224, 0.225])
        self.normalize = torchvision.transforms.Normalize(self.mean, self.stdev)
        
    def _preprocess(self, camera_value):
        x = camera_value
        x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
        x = x.transpose((2, 0, 1))
        x = torch.from_numpy(x).float()
        x = self.normalize(x)
        x = x.to(self.device)
        x = x[None, ...]
        return x
    
    def _update(self, change):
        x = change['new'] 
        x = self._preprocess(x)
        y = self.model(x)
        y = F.softmax(y, dim=1)

        prob_blocked = float(y.flatten()[0])

        if prob_blocked < 0.5:
            self.robot.forward(0.4)
        else:
            self.robot.left(0.4)
    
    def start(self):
        self.device = torch.device('cuda')
        
        print('Loading model...')
        # create model
        self.model = torchvision.models.alexnet(pretrained=False)
        self.model.classifier[6] = torch.nn.Linear(self.model.classifier[6].in_features, 2)
        self.model.load_state_dict(torch.load(self.collision_model))
        self.model = self.model.to(self.device)
    
        # create robot
        self.robot = Robot()
        
        print('Initializing camera...')
        # create camera
        self.camera = Camera.instance(width=224, height=224)
        
        print('Running...')
        self.camera.observe(self._update, names='value')
        
        def kill(sig, frame):
            print('Shutting down...')
            self.camera.stop()
            
        signal.signal(signal.SIGINT, kill)
        
        self.camera.thread.join()
        
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('collision_model', help='Path of the trained Alexnet collision model')
    args = parser.parse_args()
    
    application = WanderApplication(collision_model=args.collision_model)
    application.start()
    
    
    
    