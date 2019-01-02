import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,False)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36,True)
time.sleep(23)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36,False)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,True)
