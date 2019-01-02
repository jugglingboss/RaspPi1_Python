import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, False)
GPIO.setup(31, GPIO.OUT)
GPIO.output(31,True)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12,50)
try:
    p.start(100)
    time.sleep(24)
    p.stop()
    
except KeyboardInterrupt:
    print ("user exit")
    
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, True)
GPIO.cleanup()
