'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

entrada = str(input('Digite F-[feminino] ou M-[masculino]: ')).upper()

if entrada == 'F':
    print('F - Feminino')
elif entrada == 'M':
    print('M - Masculino')
else:
    print('Sexo Inválido')