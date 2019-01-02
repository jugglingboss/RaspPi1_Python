import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.OUT)
GPIO.output(31,False)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12,50)
p.start(50)

time.sleep(3)

p.stop()
GPIO.cleanup()