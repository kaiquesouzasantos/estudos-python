# 100/100

saida = 0

for i in range(3):
    n = int(input())

    if (n%2 == 0) or (str(n)[-1] == "5"):
        saida += 1
print(saida)
