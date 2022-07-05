# 100/100

p, d1, d2 = int(input()), int(input()), int(input())
soma, par, impar = (d1 + d2), 0, 0

if p == 0: par, impar = 0, 1
else: par, impar = 1, 0

if soma%2 == 0: print(par)
else: print(impar)

