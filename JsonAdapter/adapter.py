
import sensors.temperature
import json 
import sensors.led
class Adapter:
    def __init__(self):
        self.json_path = 'JsonAdapter/data.json'
        self.data = self.Json_Obj()
        self.temperature = self.data['temperatureSensor']
        self.ledStatus = self.data['ledStatus']['ledOn']
        self.ledValue = self.data['ledStatus']['intensive']
        self.ledType = self.data['ledStatus']['typeLigth']
    def Json_Obj(self):
        with open(self.json_path) as f:
            data = json.load(f)
            return data
    def Json_Upd(self):
        with open(self.json_path,'w') as f:
            json.dump(self.data,f)
    def temperatureUpdate(self):
        #self.temperature = sensors.temperature.get_temperature1()
        self.data['temperatureSensor'] = sensors.temperature.get_temperature2()
    def get_temperature(self):
        self.temperature = self.data['temperatureSensor']
        return self.temperature
    def ledTurnOff(self):
        self.data['ledStatus']['ledOn'] = sensors.led.LedOff()
    def ledTurnOn(self):
        self.data['ledStatus']['ledOn'] = sensors.led.LedOn()
    def get_ledStatus(self):
        self.ledStatus = self.data['ledStatus']['ledOn']
        return self.ledStatus