import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)


GPIO.setup(37,GPIO.IN)
var=1

try:
    
    while var==1:
        #print ("test3")
        if GPIO.input(37)==0:
            #print("No Motion")
            #time.sleep(5)
            #print(datetime.datetime.now())
            c=1
        else:
            print("Motion")
            print(datetime.datetime.now())
            time.sleep(.5)
except:
    KeyboardInterrupt
    print ("user exit")
    GPIO.cleanup()
    
        
    
    