n = int(input())
lista = []
total = 0

for i in range(n):
    lista.append(int(input()))

# maisCaro <para> maisBarato | sort(reverse=True)
lista.sort()
lista.reverse()

for i in range(len(lista)):
    if i % 3 == 2:
        continue # passa para o proximo elemento da lista
    total += lista[i]

print(total)