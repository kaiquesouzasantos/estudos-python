# 100/100

def verifica(aux):
    # len(5.0) -> 3, "." -> 1, 3 - 1 = 2
    if (len(aux) - aux.index(".")) == 1:
        print(aux+"00")
    elif (len(aux) - aux.index(".")) == 2:
        print(aux + "0")
    else:
        print(aux)

operacao = input()
n1, n2 = map(float, input().split())

if operacao == "M":
    verifica(str(round(n1*n2, 2)))
elif operacao == "D":
    verifica(str(round(n1/n2, 2)))