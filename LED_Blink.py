#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

led_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #gpio.board..
GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
    GPIO.output(led_pin, 1)
    print("LED_off!")
    time.sleep(1)
    GPIO.output(led_pin,0)
    print("LED_on")
    time.sleep(1)
print("program finished.")
GPIO.cleanup()
