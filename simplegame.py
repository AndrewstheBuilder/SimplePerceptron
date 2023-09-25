import pygame
from pygame.locals import *
import sys
import random
from perceptron import Perceptron

pygame.init()

# define a Perceptron
ptron = Perceptron(3)

# Constants
WIDTH, HEIGHT = 600, 600
DOT_SIZE = 4
DELAY = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize display
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Simple Game")

# Randomly generate line's slope and intercept
m = random.uniform(-1, 1)
b = random.uniform(HEIGHT//4, HEIGHT//2)


def is_above_line(x, y):
    """
    Check if point (x, y) is above the line y = m*x + b.

    Note: In computer graphics (like Pygame), the origin (0, 0) starts at the top-left
    corner of the screen. As the y-value increases, you move downwards on the screen.
    Therefore, if the given y is less than the calculated y for the line, the point
    is considered to be "above" the line in this coordinate system.
    """
    return 1 if y < m * x + b else 0


def draw_guess(x, y, guess):
    """Draw a dot on the display based on the perceptron's guess."""
    color = BLUE if guess == 1 else RED
    pygame.draw.circle(DISPLAYSURF, color, (x, y), 1)


def draw_dot(x, y, is_above):
    """Draw a dot on the display based on its class."""
    if is_above == 1:
        pygame.draw.circle(DISPLAYSURF, BLACK, (x, y),
                           DOT_SIZE, 1)  # Black outline
        pygame.draw.circle(DISPLAYSURF, WHITE, (x, y),
                           DOT_SIZE - 1)    # White inside
    else:
        pygame.draw.circle(DISPLAYSURF, BLACK, (x, y), DOT_SIZE)


# Draw dots
for _ in range(2000):
    x, y = random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)
    inputs = [x, y, 1]
    answer = is_above_line(x, y)
    ptron.train(inputs, answer)
    draw_dot(x, y, answer)

    guess = ptron.feedforward(inputs)
    draw_guess(x, y, guess)

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
