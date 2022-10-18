#!/bin/python3

from sense_hat import SenseHat
import time
from random import randint

def randColor():
    return randint(0,255)

sense = SenseHat()
sense.set_rotation(180)

sense.show_message((time.strftime("%H:%M:%S", time.localtime())), text_colour=[randColor(), randColor(), randColor()], scroll_speed=0.1)

