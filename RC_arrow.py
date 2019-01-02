import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
#GPIO.setup(35, GPIO.OUT)
#GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
#GPIO.output(31, False)
GPIO.output(29, False)
GPIO.output(38,False)
GPIO.output(40,False)
p= GPIO.PWM(12,60)
#q= GPIO.PWM(35,60)
reverse=0
forward=1
import curses

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

var=1
p.start(0)
#q.start(0)

try:
    while True:
        char = screen.getch()
        if char == ord('q'): 
            print ("user exit 2")
            var=0
            GPIO.output(38,False)
            GPIO.output(40,False)
            GPIO.output(31, False)
            GPIO.output(29, False)
            GPIO.cleanup()
            break
        elif char == curses.KEY_RIGHT:
            preturn=10
            turn=.0015+float(preturn)*.00002
            GPIO.output(8,1)
            time.sleep(.0013)
            GPIO.output(8,0)
            screen.addstr(0, 0, 'right')
        elif char == curses.KEY_LEFT:
            preturn=-10
            turn=.0015+float(preturn)*.00002
            GPIO.output(8,1)
            time.sleep(.0018)
            GPIO.output(8,0)
            screen.addstr(0, 0, 'left ')        
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up   ')
            prespeed=6
            speed= int(prespeed) * int('10')
            fspeed= float(speed)
            p.ChangeDutyCycle(fspeed)
            GPIO.output(38,0)
            GPIO.output(40,1)
            
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            prespeed=6
            speed= int(prespeed) * int('10')
            fspeed= float(speed)
            p.ChangeDutyCycle(fspeed)
            GPIO.output(40,0)
            GPIO.output(38,1)
            
        elif char == ord('s'):
            screen.addstr(0, 0, 'stop drive ')
            p.ChangeDutyCycle(0)
        elif char == ord('d'):
            screen.addstr(0, 0, 'stop turn')
            GPIO.output(8,1)
            time.sleep(.0015)
            GPIO.output(8,0)
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()


    
   




