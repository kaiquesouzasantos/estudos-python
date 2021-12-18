'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

num_1 = float(input('Digite um numero: '))

if num_1 > 0:
    print(f'{num_1} = positivo')
elif num_1 < 0: 
    print(f'{num_1} = negativo')
else:
    print(f'{num_1} = 0')

