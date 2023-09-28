import pygame
from pygame.locals import *
import sys
import random
from perceptron import Perceptron
import matplotlib.pyplot as plt

# Set the seed
# random.seed(123456)

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
DOT_SIZE = 4
DELAY = 1

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

# define a Perceptron
ptron = Perceptron(3, HEIGHT)


def is_above_line(x, y):
    """
    Check if point (x, y) is above the line y = m*x + b.

    Note: In computer graphics (like Pygame), the origin (0, 0) starts at the top-left
    corner of the screen. As the y-value increases, you move downwards on the screen.
    Therefore, if the given y is less than the calculated y for the line, the point
    is considered to be "above" the line in this coordinate system.
    """
    return 1 if y < m * x + b else -1


def draw_guess(x, y, guess):
    """Draw a dot on the display based on the perceptron's guess."""
    color = RED if guess == 1 else BLUE
    pygame.draw.circle(DISPLAYSURF, color, (x, y), 2)

def draw_dot(x, y, is_above):
    """Draw a dot on the display based on its class."""
    if is_above == 1:
        pygame.draw.circle(DISPLAYSURF, BLACK, (x, y),
                           DOT_SIZE, 1)  # Black outline
        pygame.draw.circle(DISPLAYSURF, WHITE, (x, y),
                           DOT_SIZE - 1)    # White inside
    else:
        pygame.draw.circle(DISPLAYSURF, BLACK, (x, y), DOT_SIZE)


data_points = [] # list to append data points to so it does not get cleared
guesses = {}
num_iterations = 10000

# Draw dots
for i in range(num_iterations):
    x, y = random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)
    inputs = [x, y, 1]
    answer = is_above_line(x, y)
    ptron.train(inputs, answer)
    data_points.append((x,y, answer))

    guess = ptron.feedforward(inputs)
    draw_guess(x, y, guess)
    guesses[i] = guess

    pygame.display.update()
    pygame.time.delay(DELAY)

    # Allow closing the window during drawing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
# Draw the actual data points at the end and calculate accuracy
accuracy = 0.0
correct = 0
total = len(data_points)
for i in range(len(data_points)):
    x,y,answer = data_points[i]
    if(guesses[i] == answer):
        correct += 1
    draw_dot(x, y, answer)
    pygame.display.update()
accuracy = correct/total
print("Correct:"+str(correct))
print("Total:"+str(total))
print("Accuracy:"+str(accuracy*100) + " %")
print('ptron.stats[num_iterations-1]: ',ptron.stats[num_iterations-1])
print('m: ', m)
print('b: ', b)

# Graph stats
stats = ptron.stats
for i in range(len(stats[0])):  # Assuming stats[0] contains the first weight set
    weight_values = [weight_set[i] for weight_set in stats]
    plt.plot(weight_values, label=f'Weight {i}')

plt.title("Weights over time")
plt.xlabel("Iteration")
plt.ylabel("Weight value")
plt.legend()
plt.show()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
