#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

tr = 23
ec = 24
pwmpin = 18
GPIO.setup(pwmpin, GPIO.OUT)

GPIO.setup(tr, GPIO.OUT)
GPIO.setup(ec, GPIO.IN)
p = GPIO.PWM(pwmpin, 144)
p.start(0)

GPIO.output(tr, False)
print("waiting....")
time.sleep(2)


try:
    while True:
        GPIO.output(tr, True)
        time.sleep(0.00001)
        GPIO.output(tr, False)

        while GPIO.input(ec) == 0:
            start = time.time()
        while GPIO.input(ec) == 1:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34300 / 2
        
        print(distance)
        if distance < 10:
            for dc in range(0,101,5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.01)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.01)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()

