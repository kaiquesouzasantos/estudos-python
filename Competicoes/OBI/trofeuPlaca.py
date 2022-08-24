# 100/100

pontos, encerra = list(), False

for i in range(5):
    ponto = int(input())
    pontos.append(ponto)

    if i > 0 and ponto > pontos[i-1]:
        encerra = True

    if ponto > 100 or ponto < 1:
        encerra = True

if encerra:
    print(0,0)
    exit()

maior = pontos[0]
trofeu = pontos.count(maior)

mPontos = [i for i in pontos if i != maior]

if len(mPontos) > 0:
    placa = mPontos.count(mPontos[0])
else: placa = 0

print(f'{trofeu} {placa}')
