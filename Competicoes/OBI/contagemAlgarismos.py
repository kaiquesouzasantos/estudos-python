# 100/100

def conta(x):
    global lista

    # percorre todos os numeros recebidos
    for i in x:
        nums = "0123456789"
        # percorre todos os numeros
        for j in nums:
            # se numeroR == numeroS: lista[pegaIndiceEmNums]
            if i == j: lista[nums.index(j)] += 1

n, lista = int(input()), [0]*10

for i in range(n):
    conta(input())

for i in range(len(lista)):
    print(f'{i} - {lista[i]}')