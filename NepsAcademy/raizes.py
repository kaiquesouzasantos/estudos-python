# 100/100

import math

def verifica(x):
    global saida

    if (len(x) - x.index(".")) == 4:
        saida += (x+"0\n")
    elif (len(x) - x.index(".")) == 3:
        saida += (x+"00\n")
    elif (len(x) - x.index(".")) == 2:
        saida += (x+"000\n")
    elif (len(x) - x.index(".")) == 1:
        saida += (x+"0000\n")
    else:
        saida += str(x)+"\n"

n, saida = int(input()), ""
valores = list(map(float, input().split()))

for i in valores:
    valor = math.sqrt(i)
    verifica(str(round(valor, 4)))

print(saida)