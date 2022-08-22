# 60/100

aFoto, lFoto = map(int, input().split())
n, listaMolduras = int(input()), dict()

for i in range(n):
    largura, altura = map(int, input().split())

    if largura >= lFoto and altura >= aFoto:
        listaMolduras.update({str(i+1):altura*largura})

listaMolduras = sorted(listaMolduras, key=listaMolduras.get)

if len(listaMolduras) > 0: print(listaMolduras[0])
else: print(-1)