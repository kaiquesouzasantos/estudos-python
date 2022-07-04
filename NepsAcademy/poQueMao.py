# 100/100

n, p1, p2, p3, cont = int(input()), int(input()), int(input()), int(input()), 0
lista = [p1, p2, p3]
lista.sort()

for i in lista:
    if i <= n:
        n = n - i
        cont += 1

print(cont)