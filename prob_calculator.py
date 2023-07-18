import copy
import random

class Hat:
    def __init__(self, **balls) -> None:
        self.balls = balls
        self.contents = []

        for ball, count in self.balls.items():
            for _ in range(count):
                self.contents.append(ball)

    def draw(self, num_ball):
        if num_ball >= len(self.contents):
            return self.contents

        drawn_balls = random.sample(self.contents, num_ball)
        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiments_passed = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        passed = True
        for ball, count in expected_balls.items():
            if drawn_balls.count(ball) < count:
                passed = False
                break

        if passed:
            experiments_passed += 1

    probability = experiments_passed / num_experiments
    return probability

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red": 2, "green": 1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
