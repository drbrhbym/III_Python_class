class Person:
    name = None
    height = None
    weight = None

p1 = Person()
p1.name = "Elwing"
p1.height = 178
p1.weight = 70
bmi = p1.weight / (p1.height / 100) ** 2
print(p1.name, bmi)

