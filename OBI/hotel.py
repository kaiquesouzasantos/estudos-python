# 100/100

d = int(input())
a = int(input())
n = int(input())

valor = 0
intervalo = 32 - n

if(n > 0 and n <= 31):
    if(n == 1):
        valor = 31*d
    elif(n > 1 and n < 16):
        valor = d+(a*(n-1))
        valor = valor * intervalo
    elif(n > 14):
        valor = d+(a*14)
        valor = valor * intervalo

    print(valor)