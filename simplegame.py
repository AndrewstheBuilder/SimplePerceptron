import pygame
from pygame.locals import *
import sys
import random
from perceptron import Perceptron
import matplotlib.pyplot as plt

# Set the seed
random.seed(3)

pygame.init()

# define a Perceptron
ptron = Perceptron(3)

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

def draw_decision_boundary():
    """Draw decision boundary based on assumption when Z=0 that is the decision boundary.
    Note: Z = W1*x + W2*y + W3*1 -> y = -W1*x/W2 - W3/W2"""
    x1 = 0
    y1 = int(-ptron.weights[2] / ptron.weights[1])
    # print('y1',y1)
    print('ptron.weights',ptron.weights)
    x2 = WIDTH
    y2 = int(-ptron.weights[0] * WIDTH / ptron.weights[1] - ptron.weights[2] / ptron.weights[1])

    pygame.draw.line(DISPLAYSURF, (255, 0, 0), (x1, y1), (x2, y2))

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
# Draw dots
for i in range(10000):
    x, y = random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)
    inputs = [x, y, 1]
    answer = is_above_line(x, y)
    ptron.train(inputs, answer)
    data_points.append((x,y, answer))

    # if(i % 50 == 0):
    #     # 1. Clear the screen
    #     DISPLAYSURF.fill(WHITE)

    #     # 2. Draw the updated boundary
    #     draw_decision_boundary()

    #     for x,y,answer in data_points:
    #         draw_dot(x, y, answer)
    # else:
    #     draw_dot(x, y, answer)

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
print("Accuracy:"+str(accuracy))

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
