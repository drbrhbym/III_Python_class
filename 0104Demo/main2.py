import random

def trans(card):
    transcolor = ["\u2663", "\u2666", "\u2665", "\u2660"]
    transnumber = ["A", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K"]

    return transcolor[card[0]] + transnumber[card[1]]

def score(number):
    return (number - 1) % 13

deck = []

for c in range(4):
    for n in range(13):
        card = (c, n)
        deck.append(card)


random.shuffle(deck)
print(deck)
print(len(deck))

my = deck[0]
del deck[0]
com = deck[0]
del deck[0]
print(trans(my), trans(com))

if score(my[1]) > score(com[1]):
    print("WIN")
elif score(my[1]) == score(com[1]):
     if my[0] > com[0]:
         print("WIN")
     else:
         print("LOSE")
else:
    print("LOSE")

print((-1) % 13)






