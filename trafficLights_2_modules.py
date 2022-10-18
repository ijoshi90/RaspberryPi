import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

# Module 1 GPIO Pins
green_1 = 21
amber_1 = 20
red_1 = 16

# Module 2 GPIO Pins
green_2 = 26
amber_2 = 19
red_2 = 13

def lightOn (pin):
    GPIO.output(pin, True)

def lightOff (pin):
    GPIO.output(pin, False)

# Define GPIO's
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_1, GPIO.OUT)
GPIO.setup(amber_1, GPIO.OUT)
GPIO.setup(green_1, GPIO.OUT)
GPIO.setup(red_2, GPIO.OUT)
GPIO.setup(amber_2, GPIO.OUT)
GPIO.setup(green_2, GPIO.OUT)

# Turn off all lights
def allLightsOff(signal, frame):
    allOff()
    GPIO.cleanup()
    sys.exit(0)

def amberOn():
    lightOn(amber_1)
    lightOn(amber_2)

def amberOff():
    lightOff(amber_1)
    lightOff(amber_2)

def allOff():
    amberOff()
    lightOff(red_1)
    lightOff(red_2)
    lightOff(green_1)
    lightOff(green_2)

# Crtl + c : Signal Interrupt
signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True:
    # Amber 1 & 2
    allOff()
    amberOn()
    sleep(2)

    # Green 1 On & Red 2 On
    amberOff()
    lightOn(green_1)
    lightOn(red_2)
    sleep(5)

    # Amber
    lightOff(green_1)
    lightOff(red_2)
    amberOn()
    sleep(2)

    # Green 2 On & Red 1 On
    amberOff()
    lightOn(green_2)
    lightOn(red_1)
    sleep(5)
