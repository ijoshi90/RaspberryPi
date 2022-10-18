from sense_hat import SenseHat
from time import sleep
import os

sense = SenseHat()

red = [255, 0, 0]
green = [0, 255, 0]
amber = [255, 165, 0]

def clear():
    os.system("clear")

def display_countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        sleep(1)

def display_colour(colour):
    sense.clear(colour)

def clear_hat():
    # Clear the LED matrix on sense hat
    sense.clear()

def red_on(seconds):
    clear()
    print("Red")
    display_colour(red)
    display_countdown(seconds)

def amber_on(seconds):
    clear()
    print("Amber")
    display_colour(amber)
    display_countdown(seconds)

def green_on(seconds):
    clear()
    print("Green")
    display_colour(green)
    display_countdown(seconds)

def main():
    i=0
    while (i<2):
        green_on(5)
        amber_on(2)
        red_on(5)
        amber_on(2)
        i+=1
    clear_hat()

main()
