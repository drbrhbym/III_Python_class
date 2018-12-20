

from decimal import Decimal

print(Decimal("3.14"))


a = "hello python"
print(a[0])
print(a[len(a) - 1])
print(a[-1])
print(a[1:7]) #1~6
print(a[2:])
print(a[::2])
print(a[2::2])
print(a[::-1])
print("hello" in a)

#布林
a = True
a = a and 5 >= 7 - 2 * 3
print(a)