import RPi.GPIO as GPIO



def ledControl(On):
    
    if On == True:
        print("True")
        LedOff()
    if On == False:
        print("False")
        LedOn()

def LedOff():
    GPIO.setmode(GPIO.BCM)
    OutputPin1 = 13
    OutputPin2 = 19
    GPIO.setup(OutputPin1, GPIO.OUT)
    GPIO.setup(OutputPin2, GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.output(OutputPin1, GPIO.HIGH)
    GPIO.output(OutputPin2, GPIO.HIGH)
    print("LedOn")
def LedOn():
    GPIO.setmode(GPIO.BCM)
    OutputPin1 = 13
    OutputPin2 = 19
    GPIO.setup(OutputPin1, GPIO.OUT)
    GPIO.setup(OutputPin2, GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.output(OutputPin1, GPIO.LOW)
    GPIO.output(OutputPin2, GPIO.LOW)
    print("LedOff")
