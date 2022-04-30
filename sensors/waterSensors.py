
from tokenize import Double
import board
import busio
import time
import sys
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class WaterSensors:
    ph4 = 3.11
    ph7 = 2.58
    m = - 5.641509
    b = 21.55509299

    def ec_read_voltage():
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
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
        ads = ADS.ADS1115(i2c)
        channel = AnalogIn(ads, ADS.P0)
        buf = list()
        
        for i in range(10): # Take 10 samples
            buf.append(channel.voltage)
            print(channel.voltage)
        buf.sort() # Sort samples and discard highest and lowest
        buf = buf[2:-2]
        avg = (sum(map(float,buf))/6) # Get average value from remaining 6
    
        return round(avg,2)

    def ph_get_ph():
        voltage = WaterSensors.ph_read_voltage()
        value = voltage*5.0/1024/6
        return 21.55509299 - (5.641509 * value)

    def ec_get_ec():
        sensorValue = WaterSensors.ec_read_voltage()
        Voltage = sensorValue*5/1024.0;   # Convert analog reading to Voltage
        return ((133.42/Voltage*Voltage*Voltage - 255.86*Voltage*Voltage + 857.39*Voltage)*0.5)*1000; # Convert voltage value to TDS value



   
