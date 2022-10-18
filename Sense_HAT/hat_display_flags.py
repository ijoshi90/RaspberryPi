from os import listdir
from os.path import isfile, join
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)

path = "8_bit_flags"

flagList = [f for f in listdir(path) if isfile(join(path, f))]

sense.clear()

for flag in flagList:
    sense.clear()
    print(flag)
    sense.load_image(path+"/"+flag)
    sleep (1)
sense.clear()
