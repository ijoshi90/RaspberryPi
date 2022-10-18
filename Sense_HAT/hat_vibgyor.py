from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.set_rotation(180)

def clearSenseHAT():
    sense.clear()

violet = (148, 0, 211)
indigo = (75, 0, 130)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (255, 127, 0)
red = (255, 0 , 0)
white = (255, 255, 255)

colours = [violet, indigo, blue, green, yellow, orange, red, white]

def displayColours():
    i = 0
    for x in range(8):
        for y in range (8):
            if i < 8:
                sense.set_pixel(x, y, colours[i])
                sleep(0.25)
        i+= 1

def main():
    clearSenseHAT()
    displayColours()
    sleep(2)
    clearSenseHAT()
    
main()
