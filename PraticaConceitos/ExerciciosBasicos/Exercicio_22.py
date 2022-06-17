'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

soma = 0

for i in range(0,4,1):
    num = float(input('Digite uma nota: '))
    soma += num
i+=1 
print('Media: '+soma/i)