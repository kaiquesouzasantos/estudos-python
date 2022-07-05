# 100/100

entrada, n = input().split(), input()

if n in entrada:
    print(entrada.count(n))

    for i in range(len(entrada)):
        if n == entrada[i]:
            print(i, end=' ')
else:
    print("Mia x", end="")