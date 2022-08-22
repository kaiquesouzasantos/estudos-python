# 25/100

qtdArquivos, limite = map(int, input().split())
arquivos = list(map(int, input().split()))
soma = sum(arquivos)
saida = int(soma/limite)

if(soma % limite != 0):
    saida += 1

print(saida, end='')