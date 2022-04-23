import time
import datetime
import RPi.GPIO as GPIO





def LedOn():
    GPIO.setmode(GPIO.BCM)
    OutputPins = 13
    GPIO.setup(OutputPins, GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.output(OutputPins, True)
    return 'true'
def LedOff():
    GPIO.setmode(GPIO.BCM)
    OutputPins = 13
    GPIO.setup(OutputPins, GPIO.OUT)
    GPIO.setwarnings(False)
    
    GPIO.output(OutputPins, False)
    return 'false'
