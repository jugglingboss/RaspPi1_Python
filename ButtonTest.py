import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.IN, pull_up_down=GPIO.PUD_UP)

t0=time.time()
for i in range(279):
    x= GPIO.input(35)
    if x == False:
        print('Pressed')
        break
    time.sleep(.05)
print(time.time()-t0)