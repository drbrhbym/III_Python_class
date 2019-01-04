from game import PassMachine

m = PassMachine()
while True:
    msg = "Please input:" + str(m.low) + "," + str(m.high)
    gu = int(input(msg))
    if m.guess(gu):
        print("Totall", m.times, "times")
        break