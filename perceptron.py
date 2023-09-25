import random


class Perceptron:
    def __init__(self, n):
        self.weights = [random.uniform(-1, 1) for _ in range(n)]
        self.c = 0.01

    def feedforward(self, inputs):
        total = sum(input_val * weight for input_val,
                    weight in zip(inputs, self.weights))
        return self.activate(total)

    def activate(self, total):
        return 1 if total > 0 else -1

    def train(self, inputs, desired):
        guess = self.feedforward(inputs)
        error = desired - guess
        for i, input_val in enumerate(inputs):
            self.weights[i] += self.c * error * input_val
