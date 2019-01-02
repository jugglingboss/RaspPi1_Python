
import time
import pygame
import random
pygame.mixer.init()
music = (random.randint(1,15))                         
                
pygame.mixer.music.load("/home/pi/Downloads/" + str(music) + ".mp3")
pygame.mixer.music.play()
var=1

while var:
    print(pygame.mixer.music.get_busy())
    time.sleep(5)