import random

my = int(input("[0] 蟲 [1] 雞 [2] 老虎 [3] 棒子"))
com = random.randint(0, 2)

trans = ["蟲", "雞", "老虎", "棒子"]
print("my:", trans[my])
print("com:", trans[com])

if my == (com + 1  ) % 4:
    print("you win")
elif com == (my + 1) %4:
    print("you lose")
else:
    print("平手")

