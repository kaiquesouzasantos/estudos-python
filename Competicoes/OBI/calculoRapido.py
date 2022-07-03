# 100/100

s, a, b = int(input()), int(input()), int(input())
resposta = 0

for i in range(a, b):
    num = i
    valor = sum(int(k) for k in str(num))
    if valor == s: resposta += 1
resposta+=1

if resposta == 1: print(0)
else: print(resposta)