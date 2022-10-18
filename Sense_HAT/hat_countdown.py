#!/bin/python3

from sense_hat import SenseHat
from time import sleep

from random import randint

def randColor():
    return randint(0,255)

sense = SenseHat()
sense.set_rotation(180)

for i in range(3, 0, -1):
    sense.show_letter(str(i), text_colour=[randColor(), randColor(), randColor()])
    sleep(1)

sense.show_message("Boom", text_colour=[randColor(), randColor(), randColor()], scroll_speed=0.1)
