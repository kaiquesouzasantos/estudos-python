# 100/100

palavra,vogal, consoante = input(), [], []

for i in palavra:
    if i in "aeiou": vogal.append(i)
    else: consoante.append(i)

vogal, consoante = ''.join(vogal), ''.join(consoante)

print(f"Vogais: {vogal}\nConsoantes: {consoante}")