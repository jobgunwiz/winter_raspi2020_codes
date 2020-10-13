#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
buz = 18

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(buz, GPIO.OUT)

GPIO.output(TRIG, False)
p = GPIO.PWM(buz, 1)


print("waiting for sensor to settle")
time.sleep(2)

cnt = 0
flag = 0
p.start(10)


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

        if distance < 10:
            p.ChangeFrequency(262)
            time.sleep(0.2)
            p.ChangeFrequency(1)
            time.sleep(1)
        elif distance < 20:
            p.ChangeFrequency(262)
            time.sleep(0.2)
            p.ChangeFrequency(1)
            time.sleep(2)
        elif distance < 30:
            p.ChangeFrequency(262)
            time.sleep(0.2)
            p.ChangeFrequency(1)
            time.sleep(3)
        else:
            p.ChangeFrequency(1)



except KeyboardInterrupt:
    print("measurement stopped by user")
    p.stop()
    GPIO.cleanup()
    print(cnt)
    print(flag)
