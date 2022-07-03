# 100/100

seq = {'1':0,'2':0,'3':0}

for i in range(3):
    seq[str(i+1)] = int(input())
# ordena as keys do dicionario de acordo com os valores
seq = sorted(seq, key=seq.get)

for i in seq: print(i)