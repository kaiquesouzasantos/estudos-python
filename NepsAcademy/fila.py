# 70/100

n, fila = int(input()), input().split()
r, saiu = int(input()), input().split()

saida = [i for i in fila if i not in saiu]
print(' '.join(saida))