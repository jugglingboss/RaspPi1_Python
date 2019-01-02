import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.output(31, False)
GPIO.output(29, False)
print ("test is running")
q= GPIO.PWM(35,60)
q.start(10)

try:
    GPIO.output(31, True)
    time.sleep(5)
    
except KeyboardInterrupt:
    GPIO.output(31, True)
    GPIO.cleanup()
    
GPIO.cleanup()
