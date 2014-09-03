import pygame, sys
from time import sleep
from pygame.locals import * 
import random
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0
pygame.font.init()
font = pygame.font.Font(None, 30)



pygame.init()
sizex=1920
sizey=1080
xdivision = 16
ydivision = 9
unitx = sizex/xdivision
unity = sizey/ydivision

screen = pygame.display.set_mode((sizex, sizey))
background = pygame.image.load('data/excavation.jpg')
im2= pygame.Surface(screen.get_size())
im2.fill((0, 0, 0))


while True:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 
    randomx= unitx * random.randint(0,xdivision)
    randomy= unity * random.randint(0,ydivision)
    text_surface = font.render("FPS: %f   Playtime: %f " % (clock.get_fps(),
 playtime), True, (255,255,255))
    screen.blit(text_surface, (10, 10))
    screen.blit(background, (randomx, randomy), pygame.Rect(randomx, randomy, unitx, unity))
    pygame.display.flip()
    sleep(0.1)
    screen.blit(im2, (randomx, randomy), pygame.Rect(randomx, randomy, unitx, unity))
    pygame.display.flip()
#    screen.blit((0,0,0), (randomx, randomy), pygame.Rect(randomx, randomy, 62, 62))
