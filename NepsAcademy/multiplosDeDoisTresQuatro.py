# 100/100

def verifica(n):
    global multiplos, div

    for i, valor in enumerate(div):
        if n % valor == 0: multiplos[i] += 1

rep, multiplos, div = int(input()), [0]*3, [2,3,4]

for i in range(rep):
    verifica(int(input()))

for i in multiplos:
    print(i)