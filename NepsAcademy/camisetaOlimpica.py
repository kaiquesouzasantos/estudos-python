# 100/100

competidores = int(input())
tamanhos = list(map(int, input().split())) # 1 -> pequeno, 2 -> medio
numPequeno, numMedio = int(input()), int(input())

if(tamanhos.count(1) > numPequeno or tamanhos.count(2) > numMedio):
    print('N')
else:
    print('S')