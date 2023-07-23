# 100/100

ignorado = input()
sequenciaA = list(map(int, input().split()))
sequenciaB = list(map(int, input().split()))

sequencia = list()

for i in range(len(sequenciaA)):
    if(sequenciaA[i] in sequenciaB):
        sequencia.append(sequenciaA[i])

if(sequencia == sequenciaB):
    print("S")
else:
    print("N")