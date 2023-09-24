import pygame
from pygame.locals import *
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
DOT_SIZE = 4
DELAY = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize display
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Simple Game")

# Randomly generate line's slope and intercept
m = random.uniform(-1, 1)
b = random.uniform(0, HEIGHT)

def is_above_line(x, y):
    """Check if point (x, y) is above the line."""
    return y < m * x + b

def draw_dot(x, y, is_above):
    """Draw a dot on the display based on its class."""
    if is_above:
        pygame.draw.circle(DISPLAYSURF, BLACK, (x, y), DOT_SIZE, 1) # Black outline
        pygame.draw.circle(DISPLAYSURF, WHITE, (x, y), DOT_SIZE - 1)    # White inside
    else:
        pygame.draw.circle(DISPLAYSURF, BLACK, (x, y), DOT_SIZE)

# Draw dots
for _ in range(2000):
    x, y = random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)

    draw_dot(x, y, is_above_line(x, y))

    pygame.display.update()
    pygame.time.delay(DELAY)

    # Allow closing the window during drawing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
