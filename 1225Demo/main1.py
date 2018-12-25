print("你".encode("BIG5"))
print("你".encode("utf-8"))

#f = open("a.txt", "r", encoding="utf-8")
with open("a.txt", "r", encoding="utf-8") as f:
article = f.read()
#f.close()

result = {}
total = 0
for c in article:
    total = total + 1
    c = c.lower()

    if not c in result: #第一次遇到, 才被設進result{}
        result[c] =  1
    else:
        result[c] = result[c] + 1

print(result)

prob = {}
for key in result:
    prob[key] = result[key] / total

print(prob)