# 100/100

quantidade = int (input())
valores = list()

for i in range(quantidade):
    valores.append(int(input()))

media = sum(valores) // quantidade

for valor in valores:
    print(media - valor)