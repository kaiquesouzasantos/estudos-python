# /100

quantidade = int(input())
if quantidade == 0:
    exit()

valores = list(map(int, input().split()))

operacao, primeiroItem, ultimoItem = 0, 0, quantidade - 1
somaEsquerda, somaDireita = valores[primeiroItem], valores[ultimoItem]

while(primeiroItem <= ultimoItem):
    if(somaEsquerda == somaDireita):
        # se os valores sao iguais, diminuo o range de busca
        primeiroItem += 1
        ultimoItem -= 1
        somaEsquerda, somaDireita = valores[primeiroItem], valores[ultimoItem]
    elif(somaEsquerda < somaDireita):
        # se a direita e maior, entao eu somo os valores da esquerda
        # adiciono o proximo item a soma de valores
        primeiroItem += 1
        somaEsquerda += valores[primeiroItem]
        operacao += 1
        if(primeiroItem == ultimoItem):
            break
    else:
        # se a esquerda e maior, entao eu somo os valores da direita
        # adiciono o proximo item a soma de valores
        ultimoItem -= 1
        somaDireita += valores[ultimoItem]
        operacao += 1
        if (primeiroItem == ultimoItem):
            break

print(operacao)