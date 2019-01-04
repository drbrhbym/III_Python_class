def add_advanced(n1, n2, n3=1, n4=1):
    return (n1 + n2) *n3 / n4
print(add_advanced(1, 2, n4=2))

def bmi(h ,w):
    return w / (h / 100) **2
print(bmi(175, 75))
print(round(bmi(175, 75), 2))


class Person:
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def cbmi(self):
        return self.weight / (self.height / 100) **2

p1 = Person("Elwing", 175, 75)
print(p1.name, p1.cbmi())

p2 = Person("Bob", 180, 75)
print(p2.name, p2.cbmi())