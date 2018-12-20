times = 0
while times < 10:
    print(2 * times + 1, "hello")
    times = times + 1


result = 0
times = 0
while times < 10:
    result = result + (times + 1)
    times += 1
print(result)


times = 0
while times < 10:
    if times == 0:
        first = 0
        ans = 0
    elif times == 1:
        second = 1
        ans = 1
    else:
        ans = first + second
        first = second
        second = ans
    print("第", times + 1, ":", ans)

    times += 1


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











