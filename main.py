import sensors.led
import requests

#while(True):
print("Honza pidor")
x = sensors.led.getLedStatus()
z = sensors.led.sum(5,6)
print(x)
