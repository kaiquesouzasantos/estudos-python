'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
cont = 0
soma = 0
opcao = 0

while opcao < 2:
    soma += float(input('Digite uma nota: '))
    cont += 1
    opcao = int(input('Quer continuar? [1 = SIM] [2 = NAO]: '))

media = soma/cont
print(f'MEDIA: {media}')

