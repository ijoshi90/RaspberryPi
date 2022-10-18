# https://simonprickett.dev/playing-with-raspberry-pi-traffic-lights/

import RPi.GPIO as GPIO
import time
import signal
import sys

green = 16
amber = 20
red = 21

# Define GPIO's
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(amber, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

# Turn off all lights
def allLightsOff(signal, frame):
    GPIO.output(red, False)
    GPIO.output(amber, False)
    GPIO.output(green, False)
    GPIO.cleanup()
    sys.exit(0)

# Crtl + c : Signal Interrupt
signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True:
    # Red
    GPIO.output(red, True)
    time.sleep(3)
    # Red and amber
    GPIO.output(amber, True)
    time.sleep(1)
    # Green
    GPIO.output(red, False)
    GPIO.output(amber, False)
    GPIO.output(green, True)
    time.sleep(5)
    # Amber
    GPIO.output(green, False)
    GPIO.output(amber, True)
    time.sleep(2)
    # Amber off (red comes on at top of loop)
    GPIO.output(amber, False)
