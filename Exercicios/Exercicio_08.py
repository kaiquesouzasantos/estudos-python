'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

preco_1 = float(input('Numero 1: '))
preco_2 = float(input('Numero 2: '))
preco_3 = float(input('Numero 3: '))

estrutura = [preco_1,preco_2,preco_3]

print(min(estrutura))
print(min(preco_1,preco_2,preco_3))