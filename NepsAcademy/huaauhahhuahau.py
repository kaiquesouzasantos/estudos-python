# 100/100

palavra = input()
saida = ""

for c in palavra:
    if c in "aieou": saida += c

# verifica se as vogais sao um palindromo
if saida == saida[::-1]: print("S")
else: print("N")