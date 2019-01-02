import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.output(31, False)
GPIO.output(29, False)
GPIO.output(38,False)
GPIO.output(40,False)
p= GPIO.PWM(12,60)
q= GPIO.PWM(35,60)
reverse=0
forward=1
var=1
p.start(0)
q.start(0)

while var==1:
    try:
        prespeed= input("Type a number 1=slow, 2=median, 10=fast and neg. for reverse  ")
        if int(prespeed)<0:
            prespeed=int(prespeed)*int(-1)
            reverse=1
            forward=0
        else:
            reverse=0
            forward=1
    except (KeyboardInterrupt, SystemExit):
        print ("user exit")
        var=0
        GPIO.output(38,False)
        GPIO.output(40,False)
        GPIO.output(31, False)
        p.stop()
        q.stop()
        GPIO.cleanup()
        
    speed= int(prespeed) * int('10')
    
    fspeed= float(speed)
    p.ChangeDutyCycle(fspeed)
    q.ChangeDutyCycle(fspeed)


    try:
        GPIO.output(38, reverse)
        GPIO.output(40,forward)
        GPIO.output(31, True)
        #time.sleep(5)
    
    except KeyboardInterrupt:
        print ("user exit 2")
        var=0
        GPIO.output(38,False)
        GPIO.output(40,False)
        GPIO.output(31, False)
        GPIO.cleanup()



