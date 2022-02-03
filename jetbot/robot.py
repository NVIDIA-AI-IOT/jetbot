# Modified by SparkFun Electronics June 2021
# Author: Wes Furuya
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warrranty of
# MERCHANABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/license>
#
#==================================================================================
# Copyright (c) 2021 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#==================================================================================

import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
import qwiic
from Adafruit_MotorHAT import Adafruit_MotorHAT
from .motor import Motor

# Scan for devices on I2C bus
addresses = qwiic.scan()

class Robot(SingletonConfigurable):

    left_motor = traitlets.Instance(Motor)
    right_motor = traitlets.Instance(Motor)
    
    
    # config
    i2c_bus = traitlets.Integer(default_value=1).tag(config=True)
    left_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    right_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)

    # Adafruit Hardware
    if 96 in addresses:
            
            def __init__(self, *args, **kwargs):
                super(Robot, self).__init__(*args, **kwargs)
                self.motor_driver = Adafruit_MotorHAT(i2c_bus=self.i2c_bus)
                self.left_motor = Motor(self.motor_driver, channel=self.left_motor_channel, alpha=self.left_motor_alpha)
                self.right_motor = Motor(self.motor_driver, channel=self.right_motor_channel, alpha=self.right_motor_alpha)
                
            def set_motors(self, left_speed, right_speed):
                self.left_motor.value = left_speed
                self.right_motor.value = right_speed
                
            def forward(self, speed=1.0, duration=None):
                self.left_motor.value = speed
                self.right_motor.value = speed

            def backward(self, speed=1.0):
                self.left_motor.value = -speed
                self.right_motor.value = -speed

            def left(self, speed=1.0):
                self.left_motor.value = -speed
                self.right_motor.value = speed

            def right(self, speed=1.0):
                self.left_motor.value = speed
                self.right_motor.value = -speed

            def stop(self):
                self.left_motor.value = 0
                self.right_motor.value = 0

    # SparkFun Hardware
    elif 93 in addresses:
                
            def __init__(self, *args, **kwargs):
                super(Robot, self).__init__(*args, **kwargs)
                
                self.motor_driver = qwiic.QwiicScmd()
                self.left_motor = Motor(self.motor_driver, channel=self.left_motor_channel, alpha=self.left_motor_alpha)
                self.right_motor = Motor(self.motor_driver, channel=self.right_motor_channel, alpha=self.right_motor_alpha)
                self.motor_driver.enable()
                
            def set_motors(self, left_speed, right_speed):
                self.left_motor.value = left_speed
                self.right_motor.value = right_speed
                self.motor_driver.enable()
        
            # Set Motor Controls: .set_drive( motor number, direction, speed)
            # Motor Number: A = 0, B = 1
            # Direction: FWD = 0, BACK = 1
            # Speed: (-255) - 255 (neg. values reverse direction of motor)
            
            def forward(self, speed=1.0, duration=None):
                speed = int(speed*255)
                self.motor_driver.set_drive(0, 0, speed)
                self.motor_driver.set_drive(1, 0, speed)
                self.motor_driver.enable()

            def backward(self, speed=1.0):
                speed = int(speed*255)
                self.motor_driver.set_drive(0, 1, speed)
                self.motor_driver.set_drive(1, 1, speed)
                self.motor_driver.enable()

            def left(self, speed=1.0):
                speed = int(speed*255)
                self.motor_driver.set_drive(0, 1, speed)
                self.motor_driver.set_drive(1, 0, speed)
                self.motor_driver.enable()

            def right(self, speed=1.0):
                speed = int(speed*255)
                self.motor_driver.set_drive(0, 0, speed)
                self.motor_driver.set_drive(1, 1, speed)
                self.motor_driver.enable()

            def stop(self):
                self.motor_driver.set_drive(0, 0, 0)
                self.motor_driver.set_drive(1, 1, 0)
                self.motor_driver.disable()