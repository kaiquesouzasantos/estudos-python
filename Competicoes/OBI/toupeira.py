# 100/100

S, T = map(int, input().split())
grafo = [[False]*S]*S
resposta = -1

for i in range(T):
    x, y = (int(i) - 1 for i in input().split())

    grafo[x][y] = True
    grafo[y][x] = True

for i in range(int(input())):
    ignorado, *sugestao = (int(i) - 1 for i in input().split())

    for k in range(ignorado):
        x, y = sugestao[k:k+2]

        if not grafo[x][y] or not grafo[y][x]:
            break
    else:
        resposta += 1

if(resposta == -1): resposta = 0
print(resposta)