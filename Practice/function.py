def add_multiple(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_multiple(3, 4, 5))

def test(*args):
    print(args)
test(3, 4, 5, 6, 7)

def test(**kwargs):
    print(kwargs)
test(a = 3, b = 4, c = 5)




def bmi(height, weight, **kwargs):
    bmi = weight / (height / 100) **2

    if "rounded" in kwargs:
        return round(bmi, kwargs["rounded"])
    else:
        return bmi

print(bmi(178, 70))
print(bmi(178, 70, rounded=2))


class Person:
    name = None
    height = None
    weight = None

    def bmi(self):
        return self.weight / ( self.height / 100) ** 2

p1 = Person()
p1.name = "Kay"
p1.height = 178
p1.weight = 70
print(p1.name, p1.bmi())


class Person:

    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

p1 = Person("alen", 178, 70)
print(p1.name, p1.bmi())





