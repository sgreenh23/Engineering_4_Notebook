import pygame
import sys
from random import *

blue = [0, 0, 255]

pygame.init()
pygame.display.set_caption('SHOAPLHLIIAE')

screen = pygame.display.set_mode((1000,1000))

screen.fill(blue)

for count in range(4096):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    rand_positionx = randint(0,990)
    rand_positiony = randint(0,990)
    pygame.draw.rect(screen, random_color, (rand_positionx, rand_positiony,10,10), 0)
pygame.display.update()

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
