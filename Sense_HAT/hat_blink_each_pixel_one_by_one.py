from sense_hat import SenseHat
from time import sleep
import os
from random import randint

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

def colourOfPixel():
    return randint(0,255), randint(0,255), randint(0,255)

def clearPixelColour():
    return (0, 0, 0)

def blinkPixelsOneByOne(start, end, increment):    
    for x in range (start, end, increment):
        for y in range (start, end, increment):
            sense.set_pixel(x, y, (colourOfPixel()))
            sleep(0.1)
            sense.set_pixel(x, y, (clearPixelColour()))
    
def main():
    blinkPixelsOneByOne(0, 8, 1)
    blinkPixelsOneByOne(7, -1, -1)

main()
