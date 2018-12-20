import random
low = 1
high = 1000
ans = random.randint(low, high)
times = 0
while True:
    msg = "Please input[" + str(low) + "-" + str(high) + "]:"
    guess = int(input(msg))

    times = times + 1
    if guess == ans:
        print("Bingo")
        break
    elif guess < ans:
        low = guess

    elif guess > ans:
        high = guess

print("ans = ", ans, ", you played", times, " times")