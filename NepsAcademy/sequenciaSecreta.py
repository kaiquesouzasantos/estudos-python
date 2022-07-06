# 100/100

n = int(input())
saida, ultimo = 0, 0

for i in range(n):
    novo = int(input())

    # se o novoValor != ultimoAdicionado, contabiliza á saida
    if novo != ultimo:
        saida += 1
        ultimo = novo

print(saida)