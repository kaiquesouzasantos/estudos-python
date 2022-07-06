# 100/100

n = int(input())
tabuleiroEntrada, tabuleiroSaida = [0]*n, [0]*n

for i in range(n):
    tabuleiroEntrada[i] = int(input())

for i in range(n):
    # se i > 0, soma com o anterior
    if i > 0: tabuleiroSaida[i] += tabuleiroEntrada[i - 1]
    # se i < limiteArray, soma com o proximo
    if i < n-1: tabuleiroSaida[i] += tabuleiroEntrada[i + 1]

    tabuleiroSaida[i] += tabuleiroEntrada[i]

for i in tabuleiroSaida: print(i)