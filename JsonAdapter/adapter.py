
import sensors.temperature
import json 
import sensors.led
import sensors.phSens
import sensors.ecSens
import Rpi.GPIO as GPIO
from sensors.waterSensors import WaterSensors


class Adapter:
    def __init__(self):
        self.json_path = 'JsonAdapter/data.json'
        self.data = self.Json_Obj()
        self.temperature = self.data['temperature']
        self.ledStatus = self.data['ledStatus']['ledOn']
        self.ledTimerOn = self.data['ledStatus']['lightsOn']
        self.ledTimerOff = self.data['ledStatus']['lightsOff']
        self.timer = 3.12
        self.ph = self.data["ph"]
        self.ec = self.data['ec']
        self.hum = self.data['hum']
        self.waterLvl = self.data['waterLvl']
    def Json_Obj(self):
        with open(self.json_path) as f:
            data = json.load(f)
            return data
    def Json_Upd(self):
        with open(self.json_path,'w') as f:
            json.dump(self.data,f)
    def temperatureUpdate(self):
        #self.temperature = sensors.temperature.get_temperature1()
        self.data['temperature'] = sensors.temperature.get_temperature()
    def get_temperature(self):
        self.temperature = self.data['temperature']
        return self.temperature
    def ledTurnOff(self):
        self.data['ledStatus']['ledOn'] = sensors.led.LedOff()
    def ledTurnOn(self):
        self.data['ledStatus']['ledOn'] = sensors.led.LedOn()
    def get_ledStatus(self):
        self.ledStatus = self.data['ledStatus']['ledOn']
        sensors.led.ledControl(self.ledStatus)
        return self.ledStatus
    def ledUpdateStatus(self,ledX):
        jsonLedStatus = json.loads(ledX)
        self.data['ledStatus']['ledOn'] = jsonLedStatus['ledOn']
    def phUpdate(self):
        self.data["ph"] = WaterSensors.ph_get_ph()
    def tdsUpdate(self):
        self.data['ec'] = WaterSensors.ec_get_ec()
    def humUpdate(self):
        self.data['hum'] = WaterSensors.humidity_voltage()
    def waterLevel(self):
        self.data = WaterSensors.watelLevelControl()