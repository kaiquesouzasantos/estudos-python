# 100/100

n = int(input())
escada = list(map(int, input().split()))
resposta = 1

for i in range(2, n):
    if((escada[i] - escada[i-1]) != (escada[i-1] - escada[i-2])):
        resposta+=1
    
print(resposta)