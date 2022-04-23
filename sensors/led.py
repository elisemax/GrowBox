import time
import datetime
import RPi.GPIO as GPIO





def LedOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    OutputPins = 13
    GPIO.output(OutputPins, True)
    return 'true'
def LedOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    OutputPins = 13
    GPIO.output(OutputPins, False)
    return 'false'
