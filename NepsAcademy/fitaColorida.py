ignorado = input()
fita = list(map(int, input().split()))

for i in range(len(fita)):
    if fita[i] == -1:
        fita[i] = 10 # esse 10 facilita achar o menor valor, considerando que agora ele e o maior possivel

# zero a esquerda
for i in range(1, len(fita)):
    # cria uma ordem crescente, sendo que se o valor anterior for 0, os proximos serao sub-sequentes
    # comparacao de valor, valorAnterior e Absoluto Possivel
    fita[i] = min(fita[i], fita[i-1] + 1, 9)

# zero a direita
for i in range(len(fita) -2, -1, -1):
    # baseado na mesma comparacao, diferindo o sentido
    fita[i] = min(fita[i], fita[i+1] + 1, 9)

print(*fita)