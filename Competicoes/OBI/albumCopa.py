# 100/100

n, m = int(input()), int(input()) 
figurinhas = []

for i in range(m):
    figurinhas.append(int(input()))

total = len(list(set(figurinhas)))
resposta = n - total

if(resposta > 0): print(resposta) 
else: print(0)
