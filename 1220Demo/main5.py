a = "hellohellohello"
print(a)

b = a.replace("o", "a")
print(b)

c = a.replace("l", "1", 4)
print(c)

namelist = ["kay", "alen", "joy", "andy"]
namelist.append("alen")
print(namelist)
print(namelist[-1])

newlist = [o for o in namelist if not o == "alen"]
print(newlist)