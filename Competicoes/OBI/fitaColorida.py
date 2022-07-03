fita = map(int, input().split())
fita = list(fita)

for i in range(len(fita)):
    if fita[i] == -1: 
        fita[i] = 10

# zero a esquerda
for i in range(1, len(fita)):
    fita[i] = min(fita[i], fita[i-1] + 1, 9)

# zero a direita
for i in range(len(fita) -2, -1, -1):
    fita[i] = min(fita[i], fita[i+1] + 1, 9)

for i in fita:
    print(fita[i], end=' ')

print(*fita)