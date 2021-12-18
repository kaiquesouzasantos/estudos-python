'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

num_1 = float(input('Digite um numero entre 0 e 10: '))

while num_1 > 10 or num_1 < 0:
    num_1 = float(input('Digite um numero entre 0 e 10: '))
print('Fim do Programa!')