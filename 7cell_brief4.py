import pygame, sys, re
from time import sleep
from pygame.locals import * 
from random import shuffle
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0
counter = 0
pygame.font.init()
font = pygame.font.Font(None, 30)

batch_size = 7
tiles = {}
sprites = {}


pygame.init()
sizex=1920
sizey=1080
xdivision = 16
ydivision =  9
xshuf = [i for i in range(xdivision*ydivision)]
unitx = sizex/xdivision
unity = sizey/ydivision

import os
for file in os.listdir("data/sprites"):
    if file.endswith(".png"):
        m = re.search('^(\w+)_(\d+)_(\d+).png',file)
        (spritename, spritex, spritey) = (m.group(1), int(m.group(2)), int(m.group(3)))
        print file
        print ("%s %i %i" % (spritename, spritex, spritey))
        spriteboxx = int(spritex%xdivision)
        spriteboxy = int(spritey%ydivision)
        spriteboxnumber = int((spriteboxy*xdivision)+spriteboxx)
#        sprite = pygame.image.load(os.path.join('data/sprites', file)).convert_alpha
#        size=sprite.Surface.get_size()
#        print size
#        (spritesizex,spritesizey) = sprite.get_rect()
#        print ("x=%s y=%s" % (spritesizex, spritesizey))
        tiles[spriteboxnumber] = ( spritename, spritex, spritey)


for key in tiles.keys():
    (spritename, spritex, spritey)=tiles[key]
    print ("%i %s %i %i" % (key, spritename, spritex, spritey))
 

screen = pygame.display.set_mode((sizex, sizey))
#background = pygame.image.load('data/all_on_one_no_bg.png')
background = pygame.image.load('data/plastic_reality_bg.png')
im2= pygame.Surface(screen.get_size())
#im2.fill((0, 0, 0))
#im2 = pygame.image.load('data/plastic_reality_bg.png')
im2 = pygame.image.load('data/all_on_one_no_bg.png')
screen.blit(im2,(0,0))
pygame.display.flip()

while True:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 
    shuffle(xshuf)
    for i in range(0,7):
        random_value = xshuf[i]
        try: 
#            print random_value
            (sprite_to_print,spx,spy)=tiles[random_value]
            print (sprite_to_print, spx, spy)
            print (pygame.Rect(spx,spy,120,120))
            screen.blit(im2, (spx, spy), pygame.Rect(spx, spy, 120, 120))
            text_surface = font.render("FPS: %f   Playtime: %f " % (clock.get_fps(),playtime), True, (255,255,255))
            screen.blit(text_surface, (10, 10))
#            pygame.display.flip()
            time.sleep(1)
            screen.blit(background, (spx, spy), pygame.Rect(spx, spy, sizex, sizey))
#            pygame.display.flip()
        except:
            sprite_to_print="False"

