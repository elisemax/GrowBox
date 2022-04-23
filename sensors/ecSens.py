import math
import sys
import time
from grove.adc import ADC

def TDS():
    adcX = ADC()
    value = adcX.adc.read(int(sys.argv[1]))
    if value != 0:
        voltage = value*5/1024.0
        tdsValue = (133.42/voltage*voltage*voltage-255.86*voltage*voltage+857.39*voltage)*0.5
        return tdsValue
    else:
        return 0