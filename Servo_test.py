import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)

#p=GPIO.PWM(8,50)
#p.start(7.5)


try:
    #while True:
##        p.ChangeDutyCycle(7.5)
##        time.sleep(1)
     #   p.ChangeDutyCycle(12.5)
     #   time.sleep(1)
     #   p.ChangeDutyCycle(2.5)
     #   time.sleep(1)
            GPIO.output(8,1)
            time.sleep(.0015)
            GPIO.output(8,0)
            time.sleep(2)
            
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
#GPIO.cleanup()
GPIO.cleanup()
    
        