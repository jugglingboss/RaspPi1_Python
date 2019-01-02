import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40,False)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12,50)
p.start(100)

time.sleep(3)

p.stop()

GPIO.cleanup()



