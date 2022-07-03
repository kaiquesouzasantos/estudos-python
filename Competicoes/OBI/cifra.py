def verifica(letra):
    global saida

    alfabeto = "abcdefghijklmnopqrstuvxz"
    consoante = "bcdfghjklmnpqrstvxz"
    vogais = "aeiou"
    vogaisAlbet = [0, 4, 8, 14, 20]

    if letra in vogais:
        saida += letra
        return  # passa para a proxima letra

    saida += letra

    # calcula a distancia entre a letra em relacao as vogais
    distancias = [abs(i - alfabeto.index(letra)) for i in vogaisAlbet]
    # pega vogal menos distante
    distanciaMin = min(distancias)
    # atribui á saida a vogal que corresponde a distancia minima em distancias
    saida += vogais[distancias.index(distanciaMin)]

    if letra == "z": saida += "z"
    else: saida += consoante[consoante.index(letra) + 1]

entrada = input()
saida = ""

for letra in entrada:
   verifica(letra)
print(saida)