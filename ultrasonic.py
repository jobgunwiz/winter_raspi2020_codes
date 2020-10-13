#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("waiting for sensor to settle")
time.sleep(2)

cnt = 0
flag = 0

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001) #10microsec
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
            flag = 1
        while GPIO.input(ECHO) == 1:
            stop = time.time()
            flag = 2

        check_time = stop - start
        distance = check_time *34300 / 2
        print("distance: %1f cm" %distance)
        time.sleep(0.00005)
        flag = 3
        #print(cnt)
        cnt = cnt + 1

except KeyboardInterrupt:
    print("measurement stopped by user")
    GPIO.cleanup()
    print(cnt)
    print(flag)
