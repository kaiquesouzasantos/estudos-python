# 100/100

n = int(input())
matriz, colunas = [[0]*n]*n, [0]*n
linha, indiceL, coluna, indiceC = 0, 0, 0, 0

for k in range(n):
    matriz[k] = list(map(int, input().split()))

    # coleta a maior soma e o indice da linha
    if sum(matriz[k]) > linha:
        linha, indiceL  = sum(matriz[k]), k

    for j in range(n):
        colunas[j] += matriz[k][j]

        # coleta a maior soma e o indice da coluna
        if colunas[j] > coluna:
            coluna, indiceC = colunas[j], j

print((coluna+linha) - (2 * matriz[indiceL][indiceC]))