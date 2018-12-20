person = {"name":"Elwing", "height":175, "weight":75}

print(person)

person["gender"] = "M"
print(person)

person["weight"] = person["weight"] + 5
print(person)

del person["gender"]
print(person)

for key in person:
    print("-", key, person[key])