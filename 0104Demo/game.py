import random

class PassMachine:
    def __init__(self, l = 1, h = 100):
        self.low = l
        self.high = h
        self.ans = random.randint(l, h)
        self.times = 0
    def guess(self, g):
        self.times = self.times + 1
        if g == self.ans:
            return True
        elif g > self.ans:
            self.high = g
            return False
        else:
            self.low = g
            return False