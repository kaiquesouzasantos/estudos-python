# 100/100

n = input().split()
a, b, c = n[0], n[1], n[2]

if a != b and a != c: print("A")
elif b != a and b != c: print("B")
elif c != a and c != b: print("C")
else: print("*")