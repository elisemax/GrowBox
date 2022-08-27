
import sensors.bluetoosh
import sensors.temperature
import json 
import sensors.led 
import sensors.waterSensors
import service.macAdress
from sensors.waterSensors import WaterSensors
from sensors.bluetoosh import Bluetoosh
from datetime import datetime
from sensors.led import Led

class Adapter:
    def __init__(self,first, second, third, fourth):
        self.json_path = 'JsonAdapter/data.json'
        self.ledStatus = self.setLed(first, second, third, fourth)
        self.temperature =  self.temperatureUpdate()
        self.ph = self.phUpdate()
        self.ec = self.ecUpdate()
        self.hum1 = self.humUpdate(12)
        self.hum2 = self.humUpdate(16)
        self.hum3 = self.humUpdate(20)
        self.hum4 = self.humUpdate(21)
        self.controlUnitId = "FRM-" + service.macAdress.get_mac_adress()
        self.waterlevel = self.waterLevel()
   
           
    def temperatureUpdate(self):
        temperature = sensors.temperature.get_temperature()
        return temperature
    def setLed(self,first, second, third, fourth):
        Led.ledControl(first, second, third, fourth)
        
    def phUpdate(self):
        return WaterSensors.ph_get_ph()
    def ecUpdate(self):
        return WaterSensors.ec_get_ec()
    def humUpdate(self, pinNumber):
        hum = WaterSensors.humidity_level_control(pinNumber)
        print("humidity button:")
        print(hum)
        return hum 

    def connectToWifi(self):
        print('called bluetoosh to recieve messages')
        Bluetoosh.receiveMessages()

    def waterLevel(self):
        waterLevel = WaterSensors.waterLevelControl()
        print("There is water:")
        print(waterLevel)
        return waterLevel
    
    def setPump(self, value):
        Led.setLight(22, value)
    @property
    def getTime(self):
        my_date = datetime.now()
        return str(my_date)
    @property
    def getTemperature(self):
        return self.temperature
    @property
    def getPH(self):
        return self.ph
    @property
    def getPPM(self):
        return self.ec
    @property
    def getHum(self):
        return self.hum    
    
