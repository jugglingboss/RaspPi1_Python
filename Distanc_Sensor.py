import RPi.GPIO as GPIO
import time
import pygame
import random
import datetime

GPIO.setmode(GPIO.BOARD)
TRIG = 40
ECHO = 36

GPIO.setup(37,GPIO.IN)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)
var = 1
count = 0
start = []
stop = []
output = []
while var == 1:
    try:
        hourtm = datetime.datetime.now()
        #print (hourtm.hour)
        while hourtm.hour > 22 or hourtm.hour < 10:
            print("Sleep Time Son")
            time.sleep(30)
            
        time.sleep(0.1)

        GPIO.output(TRIG,1)
        time.sleep(0.00001)
        GPIO.output(TRIG,0)

        output.append(round(((stop[count] - start[count]) *17000),2))
        #print (output)
        count = count+1
        time.sleep(.2)
        
        if count == 10:
            count = 9
            
            total = 0
            for x in range (0,9):
                total = total + output[x]
                
            avg =  total/10
            change = (output[9]-avg)/avg
            #print (change)
            print ("running")
            #if ((change > .4 or change <-.4) and GPIO.input(37)==1):
            if GPIO.input(37)==1:
                music = (random.randint(1,4))
                
                print(output)               
                pygame.mixer.init()
                pygame.mixer.music.load("/home/pi/Downloads/" + str(music) + ".mp3")
                pygame.mixer.music.play()
                pygame.mixer.music.get_busy()
                time.sleep(100)
                pygame.mixer.music.stop()
                
                print ("going for another loop")
                count=-1;
                start = [1]
                stop = [1]
                output = [1]
                print (start)
                       
            first=output[0]
            firststart=start[0]
            firststop=stop[0]
            output.remove(first)
            start.remove(firststart)
            stop.remove(firststop)

    except KeyboardInterrupt:
        var=0
        print ("user exit")
        GPIO.cleanup()

