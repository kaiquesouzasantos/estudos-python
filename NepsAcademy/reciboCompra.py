# 100/100

n = list(map(int, input().split()))
r = n[0]
k = n[1]
resposta = 0

def busca(nivel, minimo, maximo):
    global resposta
    global k

    if(nivel == k): 
        if(minimo <= maximo): 
            resposta += 1
    else:
        for i in range(minimo, maximo):
            busca(nivel+1, i+1, maximo-i)

busca(1,1,r)
print(resposta)