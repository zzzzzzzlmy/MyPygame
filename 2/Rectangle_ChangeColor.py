import pygame, sys, random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangles")

pos_x = 300
pos_y = 250
vel_x = 1
vel_y = 1
color = 255, 255, 0

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((255, 255, 255))

    #move the rectangle
    pos_x += vel_x
    pos_y += vel_y  

    #keep rectangle on the screen
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
    if pos_x == 500 or pos_x == 0:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if pos_y == 400 or pos_x == 0:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
   
    #draw the rectangle
    width = 0 #solid fill
    pos = pos_x, pos_y, 100, 100
    pygame.draw.rect(screen, color, pos, width)

    pygame.display.update()
    
    
