# 100/100

coluna1, coluna2, coluna3 = 0, 0, 0

for i in range(3):
    for k in range(3):
        num = int(input())

        if k == 0: coluna1 += num
        elif k == 1: coluna2 += num
        else: coluna3 += num

print(f'Coluna 0: {coluna1}\nColuna 1: {coluna2}\nColuna 2: {coluna3}')