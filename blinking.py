import os
import time
import sys
x= int(sys.argv[1])

#print (x)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)


#x=int(input("How many times do you want it to blink "))
for x in range(0,x):
    GPIO.output(38,True)
    time.sleep(.1)
    GPIO.output(38,False)
    GPIO.output(7,True)
    time.sleep(.1)
    GPIO.output(7,False)
    x=x+1