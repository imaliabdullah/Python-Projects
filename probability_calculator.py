import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, num):
    if num >= len(self.contents):
      return self.contents
    else:
      balls_drawn = []
      for i in range(num):
        index = random.randint(0, len(self.contents) - 1)
        ball = self.contents.pop(index)
        balls_drawn.append(ball)
      return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_successful_experiments = 0

  for i in range(num_experiments):
    hat_copy = Hat()
    hat_copy.contents = hat.contents.copy()

    balls_drawn = hat_copy.draw(num_balls_drawn)
    balls_drawn_count = Counter(balls_drawn)

    success = True
    for k, v in expected_balls.items():
      if balls_drawn_count[k] < v:
        success = False
        break

    if success:
      num_successful_experiments += 1

  probability = num_successful_experiments / num_experiments
  return probability

hat = Hat(blue=5, red=4, green=2)
expected_balls = {'red':1, 'green':2}
num_balls_drawn = 4
num_experiments = 10000

probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print("Probability:", probability)