valor = float(input())
a, f, p = float(input()), float(input()), float(input())

lista = [a, f ,p]
lista.sort()

if(sum(lista) <= valor):
    print(3)
elif(lista[0] + lista[1] <= valor):
    print(2)
elif(lista[0] <= valor):
    print(1)
else:
    print(0)