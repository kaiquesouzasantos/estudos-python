'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3: '))
nota_4 = float(input('Nota 4: '))

resultado = (nota_1+nota_2+nota_3+nota_4)/4

if resultado >= 7:
    print('APROVADO')
elif resultado <= 7:
    print('REPROVADO')
elif resultado == 10:
    print('APROVADO COM DISTICAO')
