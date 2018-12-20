#open("path", r or w or a, encoding="utf-8)

f = open("bus.json", "r", encoding="utf-8")

article = f.read()
f.close
#print(article)

#未read:load, 已read:loads

import json
buses = json.loads(article)
print(buses)

print("有幾輛車:", len(buses["datas"]) )

# buses -> dict
# buses["datas"] -> list
# b -> dict
for b in buses["datas"]:
    print(b)
    #print(b["BusID"], "(", b["Longitude"], ",", b["Latitude"], ")")