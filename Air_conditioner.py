import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinlist = [20]

for i in pinlist:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    
GPIO.output(20, GPIO.LOW)
print ("one")

GPIO.cleanup()