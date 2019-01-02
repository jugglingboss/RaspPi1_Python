import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
p= GPIO.PWM(12,60)

#GPIO.output(37, False)
#GPIO.output(35,False)

p.start(100)
GPIO.output(38,True)

time.sleep(3)

GPIO.output(38,False)
GPIO.cleanup()