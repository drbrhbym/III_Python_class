import random

win = 0
lose = 0

for times in range(0, 1000000):
    doors = ["羊", "羊"]
    c = random.randint(0, 2)
    doors.insert(c, "車")

    c = random.randint(0, 2)
    del doors[c]
    doors.remove("羊")

    if doors[0] == "車":
        win = win + 1
    else:
        lose = lose + 1
print("Total times: ", win + lose)
print("Total win: ", win)
print("Total lost: ", lose)
print("win %: ", round(win / (win + lose) * 100, 3), "%")
print("lose %: ", round(lose / (win + lose) * 100, 3), "%")