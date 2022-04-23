from w1thermsensor import W1ThermSensor

def get_temperature():
    sensor = W1ThermSensor()
    return sensor.get_temperature()
#def get_temperature1():
#    return "28"
#def get_temperature2():
#    return "54"