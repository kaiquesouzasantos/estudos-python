n = int(input())
lista = list(map(int, input().split()))

lista.sort()
deuRuim = 0
lista.insert(0, 0) 

for i in range(n):
    if(lista[i]-lista[i-1] > 8): deuRuim = 1

if(deuRuim == 1):
    print("N")
else:
    print("S")