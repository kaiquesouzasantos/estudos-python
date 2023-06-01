# /100

ignorado1, borrados, ignorado2 = map(int, input().split())
senha = input()
letras, combinacoes, contador = list(), list(), 0

for i in range(borrados):
    letras.append(input().split())

posicaoSenha = int(input()) - 1

for caracter in range(len(senha) - 1):
    if(senha[caracter] == '#'):
        for possibilidades in letras[contador]:
            for letra in possibilidades:
                senhaAuxiliar = list(senha)
                senhaAuxiliar[caracter] = letra
                print(senhaAuxiliar)
        contador += 1