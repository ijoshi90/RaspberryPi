import RPi.GPIO as GPIO
import time

fan_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)

for i in range(100000):
    print(i)
    GPIO.output(fan_pin, GPIO.HIGH)
#    GPIO.output(fan_pin, GPIO.LOW)

GPIO.cleanup()
