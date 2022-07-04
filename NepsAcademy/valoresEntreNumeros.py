# 100/100

a, b = int(input()), int(input())
lista = [a,b]
a, b = max(lista), min(lista)

for i in range(b,a+1):
    print(i, end=" ")