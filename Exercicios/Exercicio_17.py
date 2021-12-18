'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

num = int(input('Digite um numero inteiro: '))
num_fatorial = 1

while num > 0:
    num_fatorial *= num
    num -= 1
print(num_fatorial)