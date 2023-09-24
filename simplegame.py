import pygame
from pygame.locals import *
import sys

pygame.init()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((600,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Simple Game")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
