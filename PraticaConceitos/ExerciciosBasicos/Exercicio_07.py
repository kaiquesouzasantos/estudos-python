'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

num_1 = float(input('Numero 1: '))
num_2 = float(input('Numero 2: '))
num_3 = float(input('Numero 3: '))

estrutura = [num_1,num_2,num_3]

print(max(estrutura))
print(max(num_1,num_2,num_3))

print(min(estrutura))
print(min(num_1,num_2,num_3))