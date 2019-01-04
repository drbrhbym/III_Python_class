person = ("Elwing", 175, 75)

print(person)

print(person[0])
print(person[-1])
print(person[::-1])
person = person + ("Taipei", "male", "movie")
print(person)
person = person[:3] + person[4:]
print(person)