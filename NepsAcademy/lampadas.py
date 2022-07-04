# 100/100

def troca(x):
    global a,b

    if x == "1":
        if a == 1: a = 0
        else: a = 1
    else:
        if a == 1: a = 0
        else: a = 1

        if b == 1: b = 0
        else: b = 1

m = int(input())
sequencia = input().split()
a, b = 0, 0

for i in sequencia:
    troca(i)

print(f'{a}\n{b}')


