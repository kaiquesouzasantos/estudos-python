# 100/100

n = int(input())
lista = list(map(int, input().split()))

print(round(sum(lista)/len(lista), 2), end="")
