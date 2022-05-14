
from tokenize import Double
import board
import busio
import time
import sys
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO



class WaterSensors:
    ph4 = 3.11
    ph7 = 2.58
    m = - 5.641509
    b = 21.55509299

    def ec_read_voltage():
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1015(i2c)
        channel = AnalogIn(ads, ADS.P2)
        buf = list()
        
        for i in range(10): # Take 10 samples
            buf.append(channel.voltage)
        buf.sort() # Sort samples and discard highest and lowest
        buf = buf[2:-2]
        avg = (sum(map(float,buf))/6) # Get average value from remaining 6
    
        return round(avg,2)

    # Setup 

    def ph_read_voltage():
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1015(i2c,gain=2/3)
        print("with gain")
        channel = AnalogIn(ads, ADS.P0)
        

        buf = list()
        for i in range(10): # Take 10 samples
            buf.append(channel.voltage)
            
        buf.sort() # Sort samples and discard highest and lowest
        buf = buf[2:-2]
        avg = (sum(map(float,buf))/6) # Get average value from remaining 6
    
        return round(avg,2)
    
    def humidity_voltage():
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1015(i2c)
        channel = AnalogIn(ads, ADS.P3)
        buf = list()
        print("Humidity voltage:")
        print(channel.voltage)
        for i in range(10): # Take 10 samples
            buf.append(channel.voltage)
    
        buf.sort() # Sort samples and discard highest and lowest
        buf = buf[2:-2]
        avg = (sum(map(float,buf))/6) # Get average value from remaining 6
    
        return round(avg,2)

    def ph_get_ph():
        voltage = WaterSensors.ph_read_voltage()
        print("PH voltahe:")
        print(voltage)
        return 21.55509299 - (5.641509 * voltage)

    def ec_get_ec():
        sensorValue = WaterSensors.ec_read_voltage()
        print("EC sensor value:")
        print(sensorValue)
        if (sensorValue==0.0):
            return 0
        Voltage = (5/1024.0)*sensorValue;   # Convert analog reading to Voltage
        print("EC voltage:")
        print(Voltage)
        return ((133.42/Voltage*Voltage*Voltage - 255.86*Voltage*Voltage + 857.39*Voltage)*0.5)*1000; # Convert voltage value to TDS value

def waterLevelControl():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    buttonInput = 17
    GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    buttonState = GPIO.input(buttonInput)
    print(buttonState)
    if buttonState == True :
        return True
    else:
        return False
    

