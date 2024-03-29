
from tokenize import Double
import time
import sys
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import adafruit_ads1x15.ads1115 as ADS


class WaterSensors:
   # ph4 = 3.11
    #ph7 = 2.58
   # m = - 5.641509
   # b = 21.55509299

    def ec_read_voltage():
        
        adc = Adafruit_ADS1x15.ADS1115()
        value = adc.read_adc(2,gain=1)
        analog_voltage = value * (4.096/2047)
        avg = analog_voltage
        print('ec value')
        print(value)
        
        return round(avg,2)

    def ph_read_voltage():
        m = -48.4   #calibration for violet ads
        b = 15.71
        adc = Adafruit_ADS1x15.ADS1115()
        values = 0
        for x in [1,2,3,4,5]:
            value = adc.read_adc(0,gain=1,data_rate=16)
            print('ph value')
            print(value)
            values = values + value
        avg_value = values/5
        print('ph value')
        print(avg_value)
        result = m * (avg_value * 0.015 / 1000)  + b
        print('ph')
        print(result)
        
        return result
    
    
    def humidity_level_control(pinNumber):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        buttonInput = pinNumber
        GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        buttonState = GPIO.input(buttonInput)
    
        if buttonState == True :
            return False
        else:
            return True

        

    def ph_get_ph():
        pHValue = WaterSensors.ph_read_voltage()
        return pHValue

    def ec_get_ec():
        sensorValue = WaterSensors.ec_read_voltage()
        
    
        if (sensorValue == 0.0):
            return 0
        Voltage = (5 / 1024.0) * sensorValue;   # Convert analog reading to Voltage
        ppm = round(((133.42 / Voltage * Voltage * Voltage - 255.86 * Voltage * Voltage + 857.39 * Voltage) * 0.5) * 1000 / 4,2); # Convert voltage value to TDS value
        return ppm / 500
    
    def waterLevelControl():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        buttonInput = 17
        GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        buttonState = GPIO.input(buttonInput)

        if buttonState == True :
            return True
        else:
            return False
        
        
    
        

