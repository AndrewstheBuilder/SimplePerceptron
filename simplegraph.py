import random
from perceptron import Perceptron
import matplotlib.pyplot as plt

# Set the seed
# random.seed(1)
# random.seed(123456)

# Constants
WIDTH, HEIGHT = 600, 600

# Randomly generate line's slope and intercept
m = random.uniform(-1, 1)
b = random.uniform(HEIGHT // 4, HEIGHT // 2)

# define a Perceptron
ptron = Perceptron(3, HEIGHT)

def plot_decision_boundary(ax, weights):
    """Plot the perceptron's decision boundary on the given axes as a shaded region."""
    slope = -weights[0] / weights[1]
    y_intercept = -weights[2] / weights[1]

    x_vals = [i for i in range(WIDTH)]
    y_vals = [slope*x + y_intercept for x in x_vals]

    ax.fill_between(x_vals, y_vals, HEIGHT, color='red', alpha=0.3)
    ax.fill_between(x_vals, y_vals, 0, color='blue', alpha=0.3)

    return ax

def is_above_line(x, y):
    return 1 if y < m * x + b else -1

data_points = []
guesses = {}
num_iterations = 10000

above_x, above_y, below_x, below_y = [], [], [], []
colors = []

plt.ion()

chunk_size = 50

for i in range(num_iterations):
    x, y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
    inputs = [x, y, 1]
    answer = is_above_line(x, y)
    ptron.train(inputs, answer, i)
    data_points.append((x, y, answer))

    guess = ptron.feedforward(inputs)
    guesses[i] = guess

    if answer == 1:
        above_x.append(x)
        above_y.append(y)
    else:
        below_x.append(x)
        below_y.append(y)

# Plot two graphs and print out stats

# Graph weights over time
plt.ioff()

stats = ptron.stats
plt.figure()
for i in range(len(stats[0])-1):
    weight_values = [weight_set[i] for weight_set in stats]
    plt.plot(weight_values, label=f'Weight {i}')

plt.title("Weights over time")
plt.xlabel("Iteration")
plt.ylabel("Weight value")
plt.legend()

fig1, ax = plt.subplots()
ax.scatter(above_x, above_y, color='white', edgecolor='black', s=16)
ax.scatter(below_x, below_y, color='black', s=16)
plot_decision_boundary(ax, ptron.weights)
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
fig1.canvas.manager.window.setGeometry(100, 100, 600, 600)  # (x, y, width, height)

accuracy = 0.0
correct = sum([1 for key in guesses if guesses[key] == data_points[key][2]])
accuracy = correct / num_iterations

# Print stats
print("Correct:", correct)
print("Total:", num_iterations)
print("Accuracy:", accuracy * 100, "%")
print('ptron.stats[num_iterations-1]: ', ptron.stats[num_iterations - 1])
print('m: ', m)
print('b: ', b)

plt.show()
