'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

entrada = str(input('Digite uma letra/caracter: ')).upper()

if entrada == 'A' or 'E' or 'I' or 'U':
    print(f'{entrada} é uma vogal')
else:
    print(f'{entrada} é uma consoante')

