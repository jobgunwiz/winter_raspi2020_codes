#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

mota = 26
motb = 19
butp = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(mota, GPIO.OUT)
GPIO.setup(motb, GPIO.OUT)
GPIO.setup(butp, GPIO.IN)

"""
GPIO.output(mota, GPIO.HIGH)
time.sleep(2)
GPIO.cleanup()
"""

try:
    while(True):
        if input("press a to stop!") == "a":
            GPIO.output(mota, GPIO.LOW)
            GPIO.output(motb, GPIO.LOW)
            time.sleep(2)

        if GPIO.input(butp) == GPIO.HIGH:
            GPIO.output(motb, GPIO.LOW)
            GPIO.output(mota, GPIO.HIGH)
            time.sleep(2)
        else:
            GPIO.output(mota, GPIO.LOW)
            GPIO.output(motb, GPIO.HIGH)
            time.sleep(2)
        
except KeyboardInterrupt:
    print("stopped by user")
    GPIO.cleanup()

