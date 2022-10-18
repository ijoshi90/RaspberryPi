# https://simonprickett.dev/playing-with-raspberry-pi-traffic-lights/

import RPi.GPIO as GPIO
import signal
import sys
from sense_hat import SenseHat
from time import sleep
import os

sense = SenseHat()
sense.set_rotation(180)

# Specicy the GPIO number here
green = 21
amber = 20
red = 16

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

def waitSeconds(seconds):
    for i in reversed(range(0,seconds)):
        sense.show_letter(str(i))
        sleep(1)


# Loop forever
for i in range(2):
    print (i)
    # Red
    GPIO.output(red, True)
    waitSeconds(5)

    # Aamber
    GPIO.output(red, False)
    GPIO.output(amber, True)
    waitSeconds(2)

    # Green
    GPIO.output(amber, False)
    GPIO.output(green, True)
    waitSeconds(5)

    # Amber
    GPIO.output(green, False)
    GPIO.output(amber, True)
    waitSeconds(2)

# Amber off (red comes on at top of loop)
    GPIO.output(amber, False)

sense.clear()
