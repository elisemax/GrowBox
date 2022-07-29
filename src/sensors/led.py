import RPi.GPIO as GPIO


class Led:
    def __init__(self, mode):
        self.__ledStatus = self.ledControl(mode)
        
        
    @property
    def getLedStatus(self):
        return self.__ledStatus
    
    
    def ledControl(self, On):
        if On == True:
            self.LedOff()
            return True
        
        if On == False:
            self.LedOn()
            return False
        
        
    def LedOff(self):
        GPIO.setmode(GPIO.BCM)
        OutputPin1 = 13
        OutputPin2 = 19
        OutputPin3 = 5
        OutputPin4 = 6
        GPIO.setup(OutputPin1, GPIO.OUT)
        GPIO.setup(OutputPin2, GPIO.OUT)
        GPIO.setup(OutputPin3, GPIO.OUT)
        GPIO.setup(OutputPin4, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(OutputPin1, GPIO.HIGH)
        GPIO.output(OutputPin2, GPIO.HIGH)
        GPIO.output(OutputPin3, GPIO.HIGH)
        GPIO.output(OutputPin4, GPIO.HIGH)
        
        
    def LedOn(self):
        GPIO.setmode(GPIO.BCM)
        OutputPin1 = 13
        OutputPin2 = 19
        OutputPin3 = 5
        OutputPin4 = 6
        GPIO.setup(OutputPin1, GPIO.OUT)
        GPIO.setup(OutputPin2, GPIO.OUT)
        GPIO.setup(OutputPin3, GPIO.OUT)
        GPIO.setup(OutputPin4, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(OutputPin1, GPIO.LOW)
        GPIO.output(OutputPin2, GPIO.LOW)
        GPIO.output(OutputPin3, GPIO.LOW)
        GPIO.output(OutputPin4, GPIO.LOW)


