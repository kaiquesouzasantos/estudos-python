# 100/100

n, lista, saida, var = int(input()), list(map(int, input().split())), 0, 0

for i in range(1, len(lista)):
    # se o atual == anterior -> soma 1
    if lista[i] == lista[i-1]: var += 1
    # senao -> quebra de sequencia, zera tudo
    elif lista[i] != lista[i-1]: var = 0

    if saida < var: saida = var

if saida == 0: print(0)
else: print(saida+1) # soma 1 a saida, pois considera o 1° numero da sequencia

