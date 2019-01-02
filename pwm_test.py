import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
p= GPIO.PWM(35,60)
p.start(0)
for x in range (0 , 100):
    p.ChangeDutyCycle(x)
    time.sleep(.5)
    

p.stop()

GPIO.cleanup()
