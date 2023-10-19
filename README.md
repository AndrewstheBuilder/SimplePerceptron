# SimplePerceptron
- Inspired by https://natureofcode.com/book/chapter-10-neural-networks/
- Simple Perceptron Build using PyGame and a basic perceptron.
- To run run **python simplegame.py** or **python simplegraph.py**
- Checkout Merge Request #2 to see how I went from averaging 90% accuracy on the perceptron binary classifier to averaging 99% accuracy. (I thought this was cool!)
[https://github.com/AndrewstheBuilder/SimplePerceptron/pull/2]
  - Below line in perceptron.py did it. It works because we are starting the bias in the range where the y intercept of `mx + b`. `mx + b` being the input line.
  - self.weights.append(random.uniform(HEIGHT//4, HEIGHT//2)) # bias term 
