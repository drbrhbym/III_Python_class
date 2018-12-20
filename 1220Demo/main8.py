import random

inner = 0
outer = 0

for times in range(100000):

   x = random.random() * 2 - 1
   y = random.random() * 2 - 1

   print(x, y)

   if x ** 2 + y ** 2 <= 1:
      inner = inner + 1
      print("圓內")
   else:
      outer = outer + 1
      print("圓外")

print("面積:", 4 * inner / (inner + outer))