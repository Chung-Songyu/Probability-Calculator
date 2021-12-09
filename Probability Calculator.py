import copy
import random

class Hat:
  def __init__(self, **kwargs):
    contents = list()
    for k, v  in kwargs.items():
      for i in range(v):
        contents.append(k)
    self.contents = contents

  def draw(self, num):
    removed = list()
    if num > len(self.contents):
      removed = self.contents.copy()
      self.contents.clear()
    else:
      removed = random.sample(self.contents, num)
      for ball in removed:
        self.contents.remove(ball)
    return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected = list()
  for k, v in expected_balls.items():
    for i in range(v):
      expected.append(k)

  success = 0
  iteration = copy.copy(num_experiments)
  while iteration > 0:
    iteration -= 1
    temp_hat = copy.deepcopy(hat)
    drawn = temp_hat.draw(num_balls_drawn)
    try:
      for ball in expected:
        drawn.remove(ball)
    except:
      continue
    success += 1

  return success / num_experiments

# Example
random.seed(95)
hat = Hat(blue = 4, red = 2, green = 6)
probability = experiment(
  hat = hat,
  expected_balls = {"blue": 2, "red": 1},
  num_balls_drawn = 4,
  num_experiments = 3000)
print("Probability:", probability)
