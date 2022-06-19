"""
Percorra dados diversos utilizando list compreshion
"""

print('-'*60)

numeros = [[numero, numero ** 2] for numero in range(10)]
print(numeros)

print('-'*60)

string = '1231254578878789121554546'
saida = [int(caracter) for caracter in string]
print(saida)
elimina = ['1','2','8','6']
saida = [int(caracter) for caracter in string if caracter not in elimina]
print(saida)

print('-'*60)

numero = 15000
converte = [algarismo for algarismo in str(numero) if algarismo != '0']
print(converte)

print('-'*60)

numero1 = '1000'
soma1 = sum(int(algarismo) for algarismo in numero1)
print(soma1)
numero2 = '1234564978'
soma2 = sum(int(algarismo) for algarismo in numero2)
print(soma2)

print('-'*60)