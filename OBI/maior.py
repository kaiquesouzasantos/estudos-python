# 100/100

n = int(input())
m = int(input())
s = int(input())

resposta = 0

for k in range(n, m):
    numero = k
    soma = sum(int(i) for i in str(numero))
    if soma == s: resposta = numero

if resposta > 0:
    print(resposta)
else:
    print(-1)

