# /100

x, y = map(float, input().split())
saida = str(round(x**y, 4))

if (len(saida) - saida.index(".")) == 4:
    print(saida + "0")
elif (len(saida) - saida.index(".")) == 3:
    print(saida + "00")
elif (len(saida) - saida.index(".")) == 2:
    print(saida + "000")
elif (len(saida) - saida.index(".")) == 1:
    print(saida + "0000")
else:
    print(saida)
