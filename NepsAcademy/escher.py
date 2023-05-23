# 100/100

tamanho = int(input())
valores = list(map(int, input().split()))
resposta, referencia = 'S', 0

for i in range(tamanho-1):
    if(i == 0):
        referencia = valores[i] + valores[tamanho-i-1]

    if(valores[i] + valores[tamanho-i-1] != referencia):
        resposta = 'N'

print(resposta)