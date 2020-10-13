#-*- coding: utf-8-*-

import RPi.GPIO as GPIO
import time

button_pin = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while 1:
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("button pushed")
    time.sleep(0.1)


#pull up juhang...
#hardware.. juhang
#plus juhang... pullup -> always high signal if we don't push//push->low
#minus juhang... pulldown -> always low signal...// push->high
#sw... available!
