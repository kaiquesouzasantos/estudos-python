'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

num_1 = float(input('Digite o 1 numero: '))
num_2 = float(input('Digite o 2 numero: '))

if num_1 > num_2:
    print(f'{num_1} é o maior')
elif num_2 > num_1:
    print(f'{num_2} é o maior')
else:
    print('são iguais')