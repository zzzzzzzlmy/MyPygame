import pygame, sys, random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Line Random")
screen.fill((255, 255, 255))

for i in range(1000):
    drawcolor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    begin_point = (random.randint(0,600),random.randint(0,600))
    end_point = (random.randint(0,600),random.randint(0,600))
    width = random.randint(0,2)
    pygame.draw.line(screen, drawcolor, begin_point, end_point, width)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
            
            
