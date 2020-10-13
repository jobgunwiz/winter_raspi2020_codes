#-*- coding: utf-8-*-

import RPi.GPIO as GPIO
import time

button_pin = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

i=0

while i < 100:
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("button pushed")
    elif GPIO.input(button_pin) == GPIO.LOW:
        print("button not pushed")
    time.sleep(0.1)
    i = i + 1


