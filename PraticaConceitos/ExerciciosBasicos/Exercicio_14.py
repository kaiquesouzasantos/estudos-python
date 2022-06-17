'''
Faça um programa que leia 5 números e informe o maior número.
'''
num_2 = 0
for i in range(0,5):
    num_1 = float(input('Digite um numero: '))
    if num_1 > num_2:
        num_2 = num_1

print(num_2)