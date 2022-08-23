trofeu, placa = 0, 0
maior, menor = 0, 0
pontos, mPontos = list(), list()
encerra = False

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

maior = max(pontos)

for i in pontos:
    if i == maior:
        trofeu += 1

for i in pontos:
    if i != maior:
        mPontos.append(i)

for i in mPontos:
    if i == mPontos[0]:
        menor = i

    if i == menor:
        placa += 1

print(f'{trofeu} {placa}')