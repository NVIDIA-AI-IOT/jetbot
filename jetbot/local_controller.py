import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import ipywidgets
from ipywidgets.widgets.trait_types import TypedTuple
from traitlets import Bool, Int, Float, Unicode, Instance, List
from ipywidgets.widgets.widget_controller import Axis, Button
import traitlets
import time
import threading
import time


def _clamp(x):
    if x < -1.0:
        return -1.0
    elif x > 1.0:
        return 1.0
    else:
        return x
    

class LocalController(ipywidgets.VBox):
    
    index = Int(help="The id number of the controller.").tag(sync=True)
    name = Unicode(read_only=True, help="The name of the controller.").tag(sync=True)
    connected = Bool(read_only=True, help="Whether the gamepad is connected.").tag(sync=True)
    timestamp = Float(read_only=True, help="The last time the data from this gamepad was updated.").tag(sync=True)
    
    buttons = List(Instance(Button), read_only=True)
    axes = List(Instance(Axis), read_only=True)
    
    def __init__(self, index=0):
        
        pygame.init()
        
        if pygame.joystick.get_count() < 1:
            raise RuntimeError("No joystick devices found.")
            
        try:
            self._joystick = pygame.joystick.Joystick(index)
        except:
            raise RuntimeError("Could not connect to joystick with index {index}".format(index=index))
        
        name = self._joystick.get_name()
        index = self._joystick.get_id()
        num_buttons = self._joystick.get_numbuttons()
        num_axes = self._joystick.get_numaxes()
        buttons = [Button() for i in range(num_buttons)]
        axes = [Axis() for i in range(num_axes)]
        
        self.set_trait('axes', axes)
        self.set_trait('buttons', buttons)
        self.set_trait('name', name)
        self.set_trait('index', index)
        self.set_trait('connected', True)
        
        axesBox = ipywidgets.HBox(axes)
        buttonsBox = ipywidgets.HBox(buttons)
        nameLabel = ipywidgets.Label(value=name)
        
        self._init_joystick_values()
        self._thread = None
        self._running = False
        self._start()
        
        super().__init__(children=(axesBox, buttonsBox, nameLabel))
        
        
    def _init_joystick_values(self):
        for i in range(self._joystick.get_numaxes()):
            self.axes[i].set_trait('value', _clamp(self._joystick.get_axis(i)))
        for j in range(self._joystick.get_numbuttons()):
            self.buttons[i].set_trait('value', self._joystick.get_button(i))
            self.buttons[i].set_trait('pressed', self._joystick.get_button(i))
            
            
    def run(self):
        while self._running:
            
            events = pygame.event.get()
            
            timestamp = time.monotonic_ns()
            
            for event in events:
                
                if event.type == pygame.JOYAXISMOTION and event.joy == self.index:
                    axis = event.axis
                    self.set_trait('timestamp', timestamp)
                    self.axes[axis].set_trait('value', _clamp(event.value))
                elif event.type == pygame.JOYBUTTONDOWN and event.joy == self.index:
                    button = event.button
                    self.set_trait('timestamp', timestamp)
                    self.buttons[button].set_trait('value', 1.0)
                    self.buttons[button].set_trait('pressed', True)
                elif event.type == pygame.JOYBUTTONUP and event.joy == self.index:
                    button = event.button
                    self.set_trait('timestamp', timestamp)
                    self.buttons[button].set_trait('value', 0.0)
                    self.buttons[button].set_trait('pressed', False)
                
            time.sleep(0.01)
                
    
    def _start(self):
        if self._thread is None:
            self._thread = threading.Thread(target=self.run)
            self._running = True
            self._thread.start()
        
    def _stop(self):
        if self._thread is not None:
            self._running = False
            self._thread.join()
            self._thread = None
            

	
