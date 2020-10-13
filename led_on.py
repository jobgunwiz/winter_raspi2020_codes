#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pwmpin = 18

GPIO.setup(pwmpin, GPIO.OUT)

GPIO.output(pwmpin, 1)

time.sleep(2)

GPIO.cleanup()
