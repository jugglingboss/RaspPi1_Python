
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38,False)
time.sleep(.1)
GPIO.output(38,True)
