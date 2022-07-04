# 100/100

n = int(input())
ultimo, penultimo = 1, 1

if (n == 1) or (n == 2) or (n == 0):
    print("1")
else:
    for i in range(2, n+1):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        i += 1

    print(termo)