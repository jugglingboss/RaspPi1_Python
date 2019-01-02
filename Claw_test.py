import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.output(37,0)
GPIO.output(35,0)
var=0
while int(var)<2:
    var=input("1 for open, 0 for close ")
    if int(var)==1:
        GPIO.output(35,1)
        time.sleep(.5)
        GPIO.output(35,0)
    elif int(var)==0:
        GPIO.output(37,1)
        time.sleep(.4)
        GPIO.output(37,0)
    else:
        GPIO.cleanup








    

          
          



