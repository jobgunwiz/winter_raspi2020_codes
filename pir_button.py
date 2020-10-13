# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

led_g = 20
led_y = 21
sensor = 4
buttonp = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_y, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buttonp, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

print("PIR READY...")
time.sleep(5)

try:
    while True:
        if GPIO.input(buttonp) == GPIO.HIGH:
            GPIO.output(led_y, 0)
            GPIO.output(led_g, 0)
            time.sleep(0.1)
            continue

        if GPIO.input(sensor) == 1:
            GPIO.output(led_y, 1)
            GPIO.output(led_g, 0)
            #print("Motion Detected!!")
            time.sleep(0.2)

        if GPIO.input(sensor) == 0:
            GPIO.output(led_g, 1)
            GPIO.output(led_y, 0)
            time.sleep(0.2)

except KeyboardInterrupt:
    print("stopped by user")
    GPIO.cleanup()



