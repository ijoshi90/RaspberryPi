from sense_hat import SenseHat

sense = SenseHat()

def humidity():
    print("Humidity: {}".format(sense.humidity))

def temperature():
    print("Temperature : {}".format(sense.temperature))

def temperatureFromHumidiy():
    temp = sense.get_temperature_from_humidity()
    print("Temperature from Humidity: %s C" % temp)

def temperatureFromPressure():
    temp = sense.get_temperature_from_pressure()
    print("Temperature from Pressure: %s C" % temp)

def pressure():
    print("Pressure: {}".format(sense.pressure))

def main():
    temperature()
    humidity()
    #temperatureFromHumidiy()
    pressure()
    #temperatureFromPressure()
    
main()
