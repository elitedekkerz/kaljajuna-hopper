from machine import Pin, PWM
import utime

class FET():
    def __init__(self):
        self.motors = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(14, Pin.OUT), Pin(16, Pin.OUT)]
        for p in self.motors:
            p.off()

    def drive(self, output):
        self.motors[int(output)].on()
        utime.sleep(12)
        self.motors[int(output)].off()
