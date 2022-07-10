#!/usr/bin/python
''' Raspberry Pi, ADS1115, PH4502C Calibration '''
# import board
# import busio
# import time
# import sys
# import adafruit_ads1x15.ads1115 as ADS
# from adafruit_ads1x15.analog_in import AnalogIn

# # Setup 

# def read_voltage():
#     i2c = busio.I2C(board.SCL, board.SDA)
#     ads = ADS.ADS1115(i2c)
#     channel = AnalogIn(ads, ADS.P0)
#     buf = list()
        
#     for i in range(10): # Take 10 samples
#         buf.append(channel.voltage)
#     buf.sort() # Sort samples and discard highest and lowest
#     buf = buf[2:-2]
#     avg = (sum(map(float,buf))/6) # Get average value from remaining 6
    
#     return round(avg,2)

   
   