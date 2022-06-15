# 100/100

n = int(input())
entrada = input().split()

ultimo = entrada[len(entrada) - 1]

try:
    if (entrada.index("0")):
        sub = entrada[entrada.index("0")]
        entrada[entrada.index("0")] = ultimo
    elif(entrada.index("5")):
        sub = entrada[entrada.index("5")]
        entrada[entrada.index("5")] = ultimo
    
    entrada[len(entrada) - 1] = sub
    print(*entrada)
except Exception: 
    print(-1)