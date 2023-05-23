# 100/100

altura = 70
inicio, fim = int(input()), int(input())

corte = (inicio + fim) * altura/2
restanteNota = (160 * altura) - corte

if(corte > restanteNota): print(1)
elif(corte < restanteNota): print(2)
else: print(0)
