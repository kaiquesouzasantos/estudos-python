n = int(input())
cadeia = input()

saida = ""
contador = 0
ultimo = ""

ultimo = cadeia[0]

for i in range(len(cadeia)):

    if ultimo == cadeia[i]:
        contador += 1
    else:
        saida += f"{contador} {ultimo} "
        contador = 1
        ultimo = cadeia[i]
else:
    saida += f"{contador} {ultimo}"

print(saida)

