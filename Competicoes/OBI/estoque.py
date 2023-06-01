linhas, colunas = map(int, input().split())
tabela = list()

for i in range(linhas):
    tabela.append(list(map(int, input().split())))

vendas = int(input())
vendasEfetivadas = 0

for i in range(vendas):
    linha, coluna = map(int, input().split())
    item = tabela[linha-1][coluna-1]

    if(item > 0):
        vendasEfetivadas += 1
        tabela[linha-1][coluna-1] = item - 1

print(vendasEfetivadas)