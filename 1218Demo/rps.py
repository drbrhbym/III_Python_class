import random

my = int(input("[0]剪刀 [1] 石頭 [2] 布"))
com = random.randint(0, 2)

trans = ["剪刀", "石頭", "布"]
print("my:", trans[my])
print("com:", trans[com])

if my == com:
    print("平手")
elif my == (com + 1) % 3:
    print("you win")
else:
    print("you losr")
