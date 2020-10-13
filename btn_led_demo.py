#-*- coding: utf-8-*-

import RPi.GPIO as GPIO
import time

button_pin = 15
led_pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

i=0

while 1:
    if GPIO.input(button_pin) == GPIO.HIGH:
        if i == 0:
            print("button pushed")
            i = 1
        GPIO.output(led_pin, 0)
    elif GPIO.input(button_pin) == GPIO.LOW:
        if i == 1:
            print("button not pushed")
            i = 0
        GPIO.output(led_pin,1)
    #time.sleep(0.1)

GPIO.cleanup()

