# -*- coding: utf-8 -*-

import random

c = int(input("你想中幾獎?:[0] 頭獎 [1] 貳獎 [2] 參獎 [3] 肆獎 [4] 伍獎 [5] 陸獎"))
win_point = 12 - c

trans = ["頭獎", "貳獎", "參獎", "肆獎", "伍獎", "陸獎"]


def generate_ticket():
    ticket = set()
    while len(ticket) < 6:
        ticket.add(random.randint(1, 49))
    return ticket


win_ticket = generate_ticket()
print("頭彩號碼:", win_ticket)
while True:
    spe_num = random.randint(1, 49)
    if not spe_num in win_ticket:
        break
print("特別號:", spe_num)

times = 0
while True:
    my_ticket = generate_ticket()
    times += 1

    match = my_ticket.intersection(win_ticket)
    point = len(match) * 2

    check_spe = my_ticket.difference(win_ticket)
    if spe_num in check_spe:
        point = point + 1
    if point >= win_point:
        break

print("你的號碼:", my_ticket)
print("中了的數字:", match)
print("特別號有無中:", spe_num in check_spe)
# 換回0 - 3
print("買了", times, "張才中了", trans[c])