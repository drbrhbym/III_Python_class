namelist = ["kay", "alen", "joy", "andy", "joy"]
print(namelist)

namelist = namelist + ["carol"]
print(namelist)

print(namelist[1])

for n in namelist:
    print("!", n)


result = 0
for times in range(0, 10):
    result = result + (times + 1)
print(result)
