# 100/100

n = int(input())
saida = str(round(((n*n)*3.1416), 2))

if len(saida) - saida.index(".") == 1: print(saida+"00")
elif len(saida) - saida.index(".") == 2: print(saida + "0")
else: print(saida)
