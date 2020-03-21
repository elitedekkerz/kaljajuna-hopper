print("importing motor lib")
from machine import Pin, PWM

class motor():
    def __init__(self):
        self.pwm = PWM(Pin(12, Pin.OUT))
        self.m = [Pin(13, Pin.OUT), Pin(15, Pin.OUT)]

    def move(self, direction = 0):
        #parse the given direction to a float value
        direction = float(direction)

        #break
        if direction == 0:
            self.m[0].off()
            self.m[1].off()
            self.pwm.duty(0)

        #forwards
        elif direction > 0:
            self.m[0].on()
            self.m[1].off()
            self.pwm.duty(int(min(1,direction)*1024.0))

        #reverse
        else:
            self.m[0].off()
            self.m[1].on()
            self.pwm.duty(int(min(1,-direction)*1024.0))
