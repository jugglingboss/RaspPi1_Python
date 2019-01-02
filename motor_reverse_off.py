import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, False)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40,True)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12,100)
try:
    p.start(20)
    time.sleep(10)
    p.stop()
except KeyboardInterrupt:
    print ("user exit")

GPIO.setup(37, GPIO.OUT)
GPIO.output(37, True)
GPIO.cleanup()