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

batch_size = 7 # 7 Squares displayed (e.g 7 of 16*9 = 7/144 )
tiles = {}
sprite_currently_displayed = False

##### Adjust these sleep times to suit###################
sleep_time_for_none_icons = 1 # A sprite is not displayed
sleep_time_for_icons = 1  # A sprite is displayed
##########################################################

pygame.init()
#Framebuffer size: 1776 x 952
sizex=1776
sizey=952
xdivision = 16 
ydivision = 9 
xshuf = [i for i in range(xdivision*ydivision)]
unitx = sizex/xdivision
unity = sizey/ydivision


import os
ins = open( "sprite_positions.txt", "r" )
for line in ins:
    print line
    try:
        m = re.search('^(\w+)\_(\d+)\_(\d+)\.png: (\d+), (\d+)',line)
    except:
        print ("Cannot match regexp on %s " % line)
    (spritename, spritex, spritey, extentx, extenty) = (m.group(1), float(m.group(2)), float(m.group(3)), float(m.group(4)), float(m.group(5)))
#    print ("%s %f %f %i %i" % (spritename, spritex, spritey, extentx, extenty))
    spriteboxx = int(spritex%xdivision)
    spriteboxy = int(spritey%ydivision)
    print ("spriteboxx = %i spriteboxy= %i" % (spriteboxx, spriteboxy))
    spriteboxnumber = int((spriteboxy*xdivision)+spriteboxx)
    
    print ("spriteboxnumber = %i " % spriteboxnumber)
    tiles[spriteboxnumber] = ( spritename, spritex, spritey, extentx, extenty)


ins.close()

for key in tiles.keys():
    ( spritename, spritex, spritey, extentx, extenty) = tiles[key]
#    print ("%i %s %i %i" % (key, spritename, spritex, spritey))

screen = pygame.display.set_mode((sizex, sizey))
background = pygame.image.load('data/plastic_reality_bg.png').convert()
im2= pygame.Surface(screen.get_size())
#im2.fill((0, 0, 0))
im2 = pygame.image.load('data/all_on_one_no_bg.png').convert_alpha()
screen.blit(background,(0,0))
pygame.display.flip()

while True:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 
    shuffle(xshuf)
    for i in range(0,7):
        random_value = xshuf[i]
        print ("Random value %i " % random_value)
        try:
           ( spritename, spritex, spritey, extentx, extenty) = tiles[random_value]
        except:
            spritename = False 
        if (spritename):
            randomx = spritex
            randomy = spritey
            print ("%s %f,%f, %f, %f" % (spritename, randomx,randomy, extentx, extenty))
#            screen.blit(background, (0, 0))
            screen.blit(im2, (randomx, randomy), pygame.Rect(randomx, randomy, extentx, extenty))
            #text_surface = font.render("FPS: %f   Playtime: %f " % (clock.get_fps(),playtime), True, (255,255,255))
            #screen.blit(text_surface, (10, 10))
            pygame.display.flip()
#            sleep(1)
            #sleep(sleep_time_for_icons)
            sprite_currently_displayed = True
        else:
#             print ('.')
#            sleep(1)
            sleep(sleep_time_for_none_icons)
        if (sprite_currently_displayed == True):
            screen.blit(background, (0, 0))
            pygame.display.flip()
            sprite_currently_displayed = False

