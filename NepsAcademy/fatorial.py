# 100/100

def fatorial(x):
    if x == 1: return x
    else: return x * fatorial(x - 1)

n = int(input())

if n == 0: print(1)
else: print(fatorial(n))

