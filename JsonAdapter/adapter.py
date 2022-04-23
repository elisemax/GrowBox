
import sensors.temperature
import json 
import sensors.led
import sensors.phSens
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
    def Json_Obj(self):
        with open(self.json_path) as f:
            data = json.load(f)
            return data
    def Json_Upd(self):
        with open(self.json_path,'w') as f:
            json.dump(self.data,f)
    def temperatureUpdate(self):
        #self.temperature = sensors.temperature.get_temperature1()
        self.data['temperature'] = sensors.temperature.get_temperature1()
    def get_temperature(self):
        self.temperature = self.data['temperature']
        return self.temperature
    def ledTurnOff(self):
        self.data['ledStatus']['ledOn'] = sensors.led.LedOff()
    def ledTurnOn(self):
        self.data['ledStatus']['ledOn'] = sensors.led.LedOn()
    def get_ledStatus(self):
        self.ledStatus = self.data['ledStatus']['ledOn']
        return self.ledStatus
    def ledTimerControl(self,timer):
        jsonTimer = json.loads(timer)
        self.ledTimerOn = jsonTimer['lightsOn']
        self.ledTimerOff = jsonTimer['lightsOff']
    def ledUpdateStatus(self):
        self.data['ledStatus']['lightsOn'] = self.ledTimerOn
        self.data['ledStatus']['lightsOff'] = self.ledTimerOff
    def phUpdate(self):
        self.data["ph"] = sensors.phSens.read_voltage()