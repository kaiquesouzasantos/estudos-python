lin = int(input())
saida = []

for i in range(lin):
    var = int(input())

    if var == 0: saida.pop()
    else: saida.append(var)

print(sum(saida))