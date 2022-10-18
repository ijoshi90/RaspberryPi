from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

sense.set_rotation(180)

for i in range(3, 0, -1):
    sense.show_letter(str(i), text_colour=[randint(0, 255), randint(0, 255), randint(0, 255)])
    sleep (1)

sense.show_message("Sparkle",scroll_speed=0.05)

for i in range(10000):
    sleep(0.05)
    i+=1
    print (i)
    num1 = randint(0, 255)
    num2 = randint(0, 255)
    num3 = randint(0, 255)
    color = (num1, num2, num3)
    space1 = randint(0, 7)
    space2 = randint(0, 7)

    # Set on what pixel what to print
    sense.set_pixel(space1, space2, color)

# Clear the LED matrix on sense hat
sense.clear()

