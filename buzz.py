#-*- coding: utf-8 -*-

#s  gpio, ground, vcc -

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 100)

#Frq = [262,294,330,349,392,440,493,523]  #doremi...
#Frq = [330,294,262,294,330,330,330]    #airplane
Frq = [523, 523]
speed = 0.5

p.start(10)

"""
while 1:
    p.stop()
    time.sleep(speed)
    p.start(10)
    time.sleep(speed)
"""

try:
    while 1:
        for fr in Frq:
            p.ChangeFrequency(fr)
            time.sleep(speed)

except KeyboardInterrupt:
    pass
p.stop()
