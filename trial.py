from time import sleep
import os

def clear():
    os.system("clear")

def red_on(seconds):
    clear()
    print("Red")
    sleep(seconds)

def amber_on(seconds):
    clear()
    print("Amber")
    sleep(seconds)

def green_on(seconds):
    clear()
    print("Green")
    sleep(seconds)

def main():
    while (True):
        green_on(5)
        amber_on(2)
        red_on(5)
        amber_on(2)

main()
