n = int(input())
valorMaior, nomeMaior = 0, ''

for i in range(n):
    nome = input()
    valor = int(input())

    if(valor > valorMaior):
        valorMaior = valor
        nomeMaior = nome

print(f'{nomeMaior}\n{valorMaior}')
