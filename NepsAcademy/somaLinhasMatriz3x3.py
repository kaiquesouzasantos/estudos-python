# 100/100

linha1, linha2, linha3 = 0, 0, 0

for k in range(3):
    for j in range(3):
        num = int(input())

        if k == 0: linha1 += num
        elif k == 1: linha2 += num
        else: linha3 += num

print(f'Linha 0: {linha1}\nLinha 1: {linha2}\nLinha 2: {linha3}')