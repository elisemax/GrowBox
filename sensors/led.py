import RPi.GPIO as GPIO


class Led:
    def __init__(self,mode):
        self.__ledStatus = self.ledControl(mode)
    @property
    def getLedStatus(self):
        return self.__ledStatus
    def ledControl(self,On = False):
        if On == True:
            print("True")
            self.LedOff()
            return "true"
        if On == False:
            print("False")
            self.LedOn()
            return "false"
    def LedOff(self):
        GPIO.setmode(GPIO.BCM)
        OutputPin1 = 13
        OutputPin2 = 19
        GPIO.setup(OutputPin1, GPIO.OUT)
        GPIO.setup(OutputPin2, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(OutputPin1, GPIO.HIGH)
        GPIO.output(OutputPin2, GPIO.HIGH)
        print("LedOn")
    def LedOn(self):
        GPIO.setmode(GPIO.BCM)
        OutputPin1 = 13
        OutputPin2 = 19
        GPIO.setup(OutputPin1, GPIO.OUT)
        GPIO.setup(OutputPin2, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(OutputPin1, GPIO.LOW)
        GPIO.output(OutputPin2, GPIO.LOW)
        print("LedOff")
