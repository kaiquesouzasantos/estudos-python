con = int(input())
result = []

for i in range(con):
    expressao = input()
    cont = 0

    for c in expressao:
        if c == '(': cont += 1
        elif c == ')': cont -= 1
        if cont < 0: break

    if cont == 0: result.append("OK")
    else: result.append("NOK")

for i,valor in enumerate(result):
    if i != len(result) - 1:
        print(valor)
    else:
        print(valor, end="")
