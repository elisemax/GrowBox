import RPi.GPIO as GPIO


class Led:
    #def __init__(self, first, second, third, fourth):
    #    self.__ledStatus = self.ledControl(mode)
        
        
    @property
    def getLedStatus(self):
        return self.__ledStatus
    
    
    def ledControl(self, first, second, third, fourth):
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
        self.setLight(13, first)
        self.setLight(19, second)
        self.setLight(5, third)
        self.setLight(6, fourth)
        
        
    def setLight(self, pin, value):
        if value == True:
            self.LedOff(pin)
        if value == False:
            self.LedOn(pin)
        
    def LedOff(self, outputPin):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(outputPin, GPIO.OUT)
    
        GPIO.setwarnings(False)
        GPIO.output(outputPin, GPIO.HIGH)
        
        
        
    def LedOn(self, outputPin):
        GPIO.setmode(GPIO.BCM)
       
        GPIO.setup(outputPin, GPIO.OUT)
    
        GPIO.setwarnings(False)
        GPIO.output(outputPin, GPIO.LOW)
       


