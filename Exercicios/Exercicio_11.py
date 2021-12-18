'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

dia_da_semana = int(input('''
1-Domingo
2-Segunda
3-Terca
4-Quarta
5-Quinta
6-Sexta
7-Sabado
'''))

estrutura = ['undifined','1-Domingo','2-Segunda','3-Terca','4-Quarta','5-Quinta','6-Sexta','7-Sabado']

print(estrutura[dia_da_semana])