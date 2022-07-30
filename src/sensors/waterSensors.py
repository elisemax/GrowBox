
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
        
        adc = Adafruit_ADS1x15.ADS1115()
        value = adc.read_adc(1)
        analog_voltage = value * (4.096 / 2047)
        avg = analog_voltage
        return round(avg,2)

    # Setup 

    def ph_read_voltage():
        
        adc = Adafruit_ADS1x15.ADS1115()
        value = adc.read_adc(0)
        phDiff = 0.006
        k = 5.05
        avg = value * phDiff -k
        print("ph voltage:")
        print(avg)
        print("ph value")
        print(value)
        
        return round(avg,2)
    
    
    def humidity_level_control(pinNumber):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        buttonInput = pinNumber
        GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        buttonState = GPIO.input(buttonInput)
        #print("humidity level button state:")
        #print(buttonState)
        if buttonState == True :
            return True
        else:
            return False


    def ph_get_ph():
        pHValue = WaterSensors.ph_read_voltage()
        return pHValue

    def ec_get_ec():
        sensorValue = WaterSensors.ec_read_voltage()
        
    
        if (sensorValue == 0.0):
            return 0
        Voltage = (5 / 1024.0) * sensorValue;   # Convert analog reading to Voltage
        
        return round(((133.42 / Voltage * Voltage * Voltage - 255.86 * Voltage * Voltage + 857.39 * Voltage) * 0.5) * 1000 / 4,2); # Convert voltage value to TDS value

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
        

