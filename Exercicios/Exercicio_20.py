'''
Altere o programa de cálculo do fatorial, limitando o fatorial a números inteiros positivos e menores que 16.
'''

try:
    num = int(input('Digite um numero inteiro: '))
    num_fatorial = 1
    
    if num < 16:
        print('Fim do Programa!')
        while num > 0:
            num_fatorial *= num
            num -= 1
        print(num_fatorial)
    else:
        print('Fim do Programa!')
except:
    print('Fim do Programa')