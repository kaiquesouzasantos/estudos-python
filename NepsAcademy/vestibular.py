# 100/100

n, sequencia, respondido, saida = int(input()), input(), input(), 0

for i in range(n):
    if sequencia[i] == respondido[i]: saida += 1
print(saida)
