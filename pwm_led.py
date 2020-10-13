#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pwmpin = 18
GPIO.setup(pwmpin, GPIO.OUT)

p = GPIO.PWM(pwmpin, 144)
p.start(0)

try:
    while 1:
        for dc in range(0,101,5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()

