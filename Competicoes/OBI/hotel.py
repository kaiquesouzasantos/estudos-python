# 100/100

d, a, n = int(input()), int(input()), int(input())
valor, intervalo = 0, 32 - n

if n < 1 or n > 31:
    print(valor)
    exit()

if(n > 0 and n < 16):
    valor = (d+(a*(n-1))) * intervalo
else:
    valor = (d+(a*14)) * intervalo

print(valor)