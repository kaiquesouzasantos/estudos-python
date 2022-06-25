def verifica(cpf):
    if len(cpf) != 11: return "Nao"

    dig = cpf[:9]

    compara = calcula(dig)
    compara = calcula(compara, 11)

    if compara != cpf: return "Nao"
    else: return "Sim"

def calcula(digitos, posicoes = 10, soma = 0):
    for i in range(len(digitos)):
        soma = soma + (int(digitos[i]) * posicoes)
        posicoes -= 1

    soma = soma % 11

    if(soma < 2): soma = 0
    else: soma = 11 - soma

    return digitos+str(soma)

while True:
    lin = input()
    if lin == '0': break

    print(verifica(lin))