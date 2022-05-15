
import sensors.temperature
import json 
import sensors.led
import sensors.phSens
import sensors.ecSens
import sensors.waterSensors
from sensors.waterSensors import WaterSensors


class Adapter:
    def __init__(self):
        self.json_path = 'JsonAdapter/data.json'
        self.data = self.Json_Obj()
        self.temperature = self.data['temperature']
        self.ph = self.data["pH"]
        self.ec = self.data['ppm']
        self.hum = self.data['humidityPerc']
    def Json_Obj(self):
        with open(self.json_path) as f:
            data = json.load(f)
            return data
    def Json_Upd(self):
        with open(self.json_path,'w') as f:
            json.dump(self.data,f)
    def temperatureUpdate(self):
        self.data['temperature'] = sensors.temperature.get_temperature()
    def get_temperature(self):
        self.temperature = self.data['temperature']
        return self.temperature
    def ledTurnOff(self):
        self.data['lightsRealStatus'] = sensors.led.LedOff()
    def ledTurnOn(self):
        self.data['lightsRealStatus'] = sensors.led.LedOn()
    def get_ledStatus(self):
        self.ledStatus = self.data['ledStatus']['ledOn']
        sensors.led.ledControl(self.ledStatus)
        return self.ledStatus
    def ledUpdateStatus(self,ledX):
        jsonLedStatus = json.loads(ledX)
        self.data['lightsRealStatus'] = jsonLedStatus['lightsRealStatus']
    def phUpdate(self):
        self.data["pH"] = WaterSensors.ph_get_ph()
    def tdsUpdate(self):
        self.data['ppm'] = WaterSensors.ec_get_ec()
    def humUpdate(self):
        self.data['hum'] = WaterSensors.humidityGetValue()

        