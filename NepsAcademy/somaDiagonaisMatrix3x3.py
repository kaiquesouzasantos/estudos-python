# 100/100

diagonalD, diagonalE = 0, 0

for k in range(3):
    for j in range(3):
        num = int(input())

        # soma das diagonais
        if k == j: diagonalE += num

        if k == 0 and j == 2: diagonalD += num
        elif k == 1 and j == 1: diagonalD += num
        elif k == 2 and j == 0: diagonalD += num

print(f'Diagonal principal: {diagonalE}\nDiagonal secundaria: {diagonalD}')