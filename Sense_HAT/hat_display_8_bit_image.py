from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)

sense.clear()

sense.load_image("8_bit_smiley.png")

sleep (5)
sense.clear()
