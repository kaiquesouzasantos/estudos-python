# 100/100

comp, minPontos = map(int, input().split())
convidados = 0

for i in range(comp):
    pontos = list(map(int, input().split()))
    if sum(pontos) >= minPontos: convidados += 1

print(convidados)