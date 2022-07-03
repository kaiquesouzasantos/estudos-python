# 100/100

# ordena os nadadores
seq = {'1':0,'2':0,'3':0}

for i in range(3):
    seq[str(i+1)] = int(input())
# ordena as keys do dicionario de acordo com os valores
seq = sorted(seq, key=seq.get)

# out de acordo com o podio, 1°, 2° e 3° colocado.
for i in seq: print(i)
