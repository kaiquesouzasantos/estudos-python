'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

vogais = ['a', 'e', 'i', 'o', 'u']

letra = str(input("Digite uma letra: "))

if letra in vogais:
  print("Vogal")
elif letra.isalpha():
  print("Consoante")
else:
  print("Não é uma letra")