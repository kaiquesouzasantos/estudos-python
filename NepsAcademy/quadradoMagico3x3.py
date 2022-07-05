# 100/100

linha1, linha2, linha3 = 0, 0, 0
coluna1, coluna2, coluna3 = 0, 0, 0
diagonalD, diagonalE = 0, 0

for k in range(3):
    for j in range(3):
        num = int(input())

        # soma das linhas
        if k == 0: linha1 += num
        elif k == 1: linha2 += num
        elif k == 2: linha3 += num

        # soma das colunas
        if j == 0: coluna1 += num
        elif j == 1: coluna2 += num
        elif j == 2: coluna3 += num

        # soma das diagonais
        if k == j: diagonalE += num

        if k == 0 and j == 2: diagonalD += num
        elif k == 1 and j == 1: diagonalD += num
        elif k == 2 and j == 0: diagonalD += num

compara = [linha1, linha2, linha3, coluna1, coluna2, coluna3, diagonalD, diagonalE]
verifica = True

for i in range(1,len(compara)):
    if compara[i] != compara[i-1]:
        verifica = False
        break

if verifica: print("SIM")
else: print("NAO")