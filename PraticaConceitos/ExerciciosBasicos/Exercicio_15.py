'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
i = 0
soma = 0
while i < 5:
    num_1 = float(input('Digite um numero: '))
    soma += num_1
    i+=1
media = soma/5

print(f'Soma: {soma}\nMedia: {media}')
    