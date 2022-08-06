
import sensors.bluetoosh
import sensors.temperature
import json 
import sensors.led
import sensors.ecSens
import sensors.waterSensors
import service.macAdress
from sensors.waterSensors import WaterSensors
from sensors.bluetoosh import Bluetoosh
from datetime import datetime

class Adapter:
    def __init__(self,first, second, third, fourth):
        self.json_path = 'JsonAdapter/data.json'
        #  self.data = self.Json_Obj()
        self.temperature =  self.temperatureUpdate()
        self.ph = self.phUpdate()
        self.ec = self.ecUpdate()
        self.hum1 = self.humUpdate(12)
        self.hum2 = self.humUpdate(16)
        self.hum3 = self.humUpdate(20)
        self.hum4 = self.humUpdate(21)
        self.ledStatus = self.getLedStatus(first, second, third, fourth)
        self.controlUnitId = "NEWFARM001-"+service.macAdress.get_mac_adress()
        self.waterlevel = self.waterLevel()
   
           
    def temperatureUpdate(self):
      #  self.data['temperature'] = sensors.temperature.get_temperature()
        temperature = sensors.temperature.get_temperature()
        return temperature
    def getLedStatus(self,first, second, third, fourth):
        ledStatus = sensors.led.Led(lightsRealStatus)
        x = ledStatus.ledControl(lightsRealStatus)
        return x
      #  ledStatus = sensors.led.Led.ledControl(lightsRealStatus)
       # return ledStatus
    def phUpdate(self):
      #  self.data["pH"] = WaterSensors.ph_get_ph()
        return WaterSensors.ph_get_ph()
    def ecUpdate(self):
      #  self.data['ppm'] = WaterSensors.ec_get_ec()
        return WaterSensors.ec_get_ec()
    def humUpdate(self, pinNumber):
        hum = WaterSensors.humidity_level_control(pinNumber)
        return hum 
   # def idUpdate(self):
      #  self.data['controlUnitId'] = self.controlUnitId
    def connectToWifi(self):
        print('called bluetoosh to recieve messages')
        Bluetoosh.receiveMessages()

    def waterLevel(self):
        waterLevel = WaterSensors.waterLevelControl()
        return waterLevel
    @property
    def getTime(self):
        my_date = datetime.now()
       # self.data['createdAt'] = my_date
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
    @property
    def getLightsRealStatus(self):
        return self.ledStatus  
