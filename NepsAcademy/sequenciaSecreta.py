# 100/100

quantidade, sequencia, resultante, ultimo = int(input()), list(), list(), ''

for i in range(quantidade):
    sequencia.append(int(input()))

for i in range(len(sequencia)):
    if(sequencia[i] != ultimo):
        ultimo = sequencia[i]
        resultante.append(sequencia[i])

print(len(resultante))