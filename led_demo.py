#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

led_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #gpio.board..
GPIO.setup(led_pin, GPIO.OUT)

while(True):
    key = int(input("type num -> 0:off 1:on any:fin  "))
    if key == 1:
        GPIO.output(led_pin, 1) #gpio.high capital
    elif key == 0:
        GPIO.output(led_pin, 0) #gpio.low
    else:
        break

"""
for i in range(10):
    GPIO.output(led_pin, 1)
    print("LED_off!")
    time.sleep(1)
    GPIO.output(led_pin,0)
    print("LED_on")
    time.sleep(1)
"""

print("program finished.")
GPIO.cleanup()
