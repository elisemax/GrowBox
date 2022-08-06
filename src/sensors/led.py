import RPi.GPIO as GPIO


class Led:
    #def __init__(self, first, second, third, fourth):
    #    self.__ledStatus = self.ledControl(mode)
        
    
    def ledControl(first, second, third, fourth):
        OutputPin1 = 13
        OutputPin2 = 19
        OutputPin3 = 5
        OutputPin4 = 6
        
        pins = {
        "first": 13,
        "second": 19,
        "third": 5,
        "fourth": 6
        }
        Led.setLight(13, first)
        Led.setLight(19, second)
        Led.setLight(5, third)
        Led.setLight(6, fourth)
        
        
    def setLight(pin, value):
        if value == True:
            Led.LedOff(pin)
        if value == False:
            Led.LedOn(pin)
        
    def LedOff(outputPin):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(outputPin, GPIO.OUT)
    
        GPIO.setwarnings(False)
        GPIO.output(outputPin, GPIO.HIGH)
        
        
        
    def LedOn(outputPin):
        GPIO.setmode(GPIO.BCM)
       
        GPIO.setup(outputPin, GPIO.OUT)
    
        GPIO.setwarnings(False)
        GPIO.output(outputPin, GPIO.LOW)
    

       


