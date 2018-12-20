import random

n = int(input("how may doors do you want to play?"))
win = 0
lose = 0

for times in range(1000000):
    doors = ["羊"] * (n - 1)
    c = random.randint(0, n - 1)
    doors.insert(c, "車")

    c = random.randint(0, n - 1)
    del doors[c]
    doors.remove("羊")

    c = random.randint(0, len(doors) - 1)
    if doors[c] == "車":
        win = win + 1
    else:
        lose = lose + 1
print("Total times: ", win + lose)
print("Total win: ", win)
print("Total lost: ", lose)
print("win %: ", round(win / (win + lose) * 100, 3), "%")
print("lose %: ", round(lose / (win + lose) * 100, 3), "%")