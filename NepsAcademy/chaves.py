# 100/100

n, cont, ok = int(input()), 0, 1

for i in range(n):
    var = input()

    for x in var:
        if x == "{": cont += 1
        elif x == "}": cont -= 1

        if cont < 0: break

if cont == 0: print("S")
else: print("N")