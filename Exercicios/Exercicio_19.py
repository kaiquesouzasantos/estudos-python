'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

estrutura = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
soma = 0

for i in estrutura:
    soma += i

print('Maximo: '+str(max(estrutura)))
print('Minimo: '+str(min(estrutura)))
print('Soma: '+str(soma))

