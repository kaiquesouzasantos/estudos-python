# 100/100

consumo, distancia, restanteLitros = int(input()), int(input()), int(input())
resultante = float((distancia/consumo) - restanteLitros)

if(resultante < 0):
    print(0.0)
else:
    print(round(resultante, 1))