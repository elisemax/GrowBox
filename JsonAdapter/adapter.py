
import sensors.temperature
import json 
import sensors.led
import sensors.phSens
import sensors.ecSens
import sensors.waterSensors
import service.macAdress
from sensors.waterSensors import WaterSensors
from datetime import datetime

class Adapter:
    def __init__(self,lightsRealStatus):
        self.json_path = 'JsonAdapter/data.json'
      #  self.data = self.Json_Obj()
        self.temperature = self.temperatureUpdate()
        self.ph = self.phUpdate()
        self.ec = self.ecUpdate()
        self.hum = self.humUpdate()
        self.ledStatus = self.getLedStatus(lightsRealStatus=False)
        self.controlUnitId = "farm-"+service.macAdress.get_mac_adress()
    ###### ??? ######    
    # def Json_Obj(self):
    #     with open(self.json_path) as f:
    #         data = json.load(f)
    #         return data
    # def Json_Upd(self):
    #     with open(self.json_path,'w') as f:
    #         json.dump(self.data,f)
    # def ledUpdateStatus(self,ledX):
    #     jsonLedStatus = json.loads(ledX)
    #     print(jsonLedStatus)
    #     self.data['lightsRealStatus'] = jsonLedStatus['lightsRealStatus']
    # def ledTurnOff(self):
    #     self.data['lightsRealStatus'] = sensors.led.LedOff()
    # def ledTurnOn(self):
    #     self.data['lightsRealStatus'] = sensors.led.LedOn()          
    ###### ??? ######
    def createJsonObj(self,controlUnitId,lightsRealStatus,temperature,pH,ppm,hum,createdAt):
        jsonObj = {
            "controlUnitId":controlUnitId,
            "lightsRealStatus": lightsRealStatus, 
            "temperature": temperature, 
            "pH": pH, 
            "ppm": ppm,
            "hum":hum,
            "createdAt":createdAt
        }
        return jsonObj               
    def temperatureUpdate(self):
      #  self.data['temperature'] = sensors.temperature.get_temperature()
        temperature = sensors.temperature.get_temperature()
        return temperature
    def getLedStatus(self,lightsRealStatus):
        ledStatus = sensors.led.Led.ledControl(self,lightsRealStatus)
        return ledStatus
    def phUpdate(self):
      #  self.data["pH"] = WaterSensors.ph_get_ph()
        return WaterSensors.ph_get_ph()
    def ecUpdate(self):
      #  self.data['ppm'] = WaterSensors.ec_get_ec()
        return WaterSensors.ec_get_ec()
    def humUpdate(self):
       # self.data['soilHumidityPerc'] = WaterSensors.humidityGetValue()
        hum = WaterSensors.humidityGetValue()
        return hum 
   # def idUpdate(self):
      #  self.data['controlUnitId'] = self.controlUnitId
    @property
    def getTime(self):
        my_date = datetime.now()
       # self.data['createdAt'] = my_date
        return my_date
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
