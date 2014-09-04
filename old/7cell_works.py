import pygame, sys
from time import sleep
from pygame.locals import * 
import random
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0
counter = 0
pygame.font.init()
font = pygame.font.Font(None, 30)

batch_size = 7
tiles = {}


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
    if ( counter < batch_size ):
        tiles[counter] = (randomx,randomy)
        screen.blit(background, (randomx, randomy), pygame.Rect(randomx, randomy, unitx, unity))
        text_surface = font.render("FPS: %f   Playtime: %f " % (clock.get_fps(),playtime), True, (255,255,255))
        screen.blit(text_surface, (10, 10))
    else:
        pygame.display.flip()
        sleep(1)
        counter = 0
        for (x,y) in tiles.values():
            print (x,y)
            screen.blit(im2, (x, y), pygame.Rect(x, y, unitx, unity))
        pygame.display.flip()
    counter +=1 
