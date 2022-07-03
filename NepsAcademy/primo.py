# 100/100

def verifica(x):
    div = 0
    for i in range(1, x):
        if x % i == 0: div += 1
    return div

def primo(x) -> bool:
    if x == 0 or x == 1 or verifica(x) > 1:
        return False
    return True

n = int(input())

if primo(n): print("S")
else: print("N")