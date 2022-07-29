
from tokenize import Double
import time
import sys
import RPi.GPIO as GPIO
import Adafruit_ADS1x15


class WaterSensors:
    ph4 = 3.11
    ph7 = 2.58
    m = - 5.641509
    b = 21.55509299

    def ec_read_voltage():
        
        adc = Adafruit_ADS1x15.ADS1115(address = 0x48)
        value = adc.read_adc(2,gain = 2/3)
        analog_voltage = value * (4.096 / 2047)
        avg = analog_voltage
        return round(avg,2)

    # Setup 

    def ph_read_voltage():
        
        adc = Adafruit_ADS1x15.ADS1115(address = 0x48)
        value = adc.read_adc(0,gain=2/3)
        phDiff = 0.006
        k = 5.05
        avg = value * phDiff -k
        print("ph voltage:")
        print(avg)
        
        return round(avg,2)
    
    
    def humidity_level_control(pinNumber):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        buttonInput = pinNumber
        GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        buttonState = GPIO.input(buttonInput)
        print("humidity level button state:")
        print(buttonState)
        if buttonState == True :
            return True
        else:
            return False
    
    def humidity_voltage(pinNumber):
        adc = Adafruit_ADS1x15.ADS1115(address = 0x49)
        value = adc.read_adc(pinNumber,gain=2/3)
        analog_voltage = value * (4.096 / 2047)
        avg = analog_voltage
        return round(avg,2)
    
    def humidityGetValue(pinNumber):
        voltage = WaterSensors.humidity_voltage(pinNumber)
        print('humidity voltage in pin numbe')
        print(pinNumber)
        print(voltage)
        min = 3.96
        max = 0.8
        abs = voltage - max

        num = (voltage - max) / (min - max)
        result = round((num - 1.0) * ( -1 ) * 100,2)
        print("humidity: ")
        print(result)
        return result


    def ph_get_ph():
        pHValue = WaterSensors.ph_read_voltage()
        return pHValue

    def ec_get_ec():
        sensorValue = WaterSensors.ec_read_voltage()
        
    
        if (sensorValue == 0.0):
            return 0
        Voltage = (5 / 1024.0) * sensorValue;   # Convert analog reading to Voltage
        print("ppm voltage:")
        print(Voltage)
        
        return round(((133.42 / Voltage * Voltage * Voltage - 255.86 * Voltage * Voltage + 857.39 * Voltage) * 0.5) * 1000 / 4,2); # Convert voltage value to TDS value

    def waterLevelControl():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        buttonInput = 17
        GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        buttonState = GPIO.input(buttonInput)
        print("water level button state:")
        print(buttonState)
        if buttonState == True :
            return True
        else:
            return False
        

