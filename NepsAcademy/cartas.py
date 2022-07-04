# 100/100

carta1, carta2, carta3, diferente = int(input()), int(input()), int(input()), 0
lista = [carta1, carta2, carta3]

for i in lista:
    if lista.count(i) == 1:
        print(i)
        break
