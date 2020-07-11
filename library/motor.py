import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT
import traitlets
from traitlets.config.configurable import Configurable


class Motor(Configurable):

    value = traitlets.Float()
    
    # config
    alpha = traitlets.Float(default_value=1.0).tag(config=True)
    beta = traitlets.Float(default_value=0.0).tag(config=True)

    def __init__(self, driver, channel, *args, **kwargs):
        super(Motor, self).__init__(*args, **kwargs)  # initializes traitlets

        self._driver = driver
        self._motor = self._driver.getMotor(channel)
        atexit.register(self._release)
        
    @traitlets.observe('value')
    def _observe_value(self, change):
        self._write_value(change['new'])

    def _write_value(self, value):
        """Sets motor value between [-1, 1]"""
        mapped_value = int(255.0 * (self.alpha * value + self.beta))
        speed = min(max(abs(mapped_value), 0), 255)
        self._motor.setSpeed(speed)
        if mapped_value < 0:
            self._motor.run(Adafruit_MotorHAT.FORWARD)
        else:
            self._motor.run(Adafruit_MotorHAT.BACKWARD)

    def _release(self):
        """Stops motor by releasing control"""
        self._motor.run(Adafruit_MotorHAT.RELEASE)
