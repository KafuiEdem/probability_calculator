import copy
import random

# Consider using the modules imported above.

class Hat:
    def __init__(self,**kw) -> None:
        self.balls=kw
        self.contents = []

        for list in self.balls:
            self.contents.append(list)

    def draw(self,num_ball):
        lup = []
        if num_ball < len(self.contents):
            return self.contents
        else:
            for _ in range(0,num_ball):
                c = random.choice(self.contents)
                lup.append(c)
                p = set(self.contents) ^ set(lup)
            return lup
       
        # return random.choice(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    c = []
    count = 0
    ball = hat.draw(num_balls_drawn)
    for b in expected_balls:
        c.append(b)
    
    for i in ball:
        for u in c:
            if i == u:
                count +=1
                file = f"{u}:{count}"
    return file


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)