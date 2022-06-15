# 100/100

verificacao = []
 
for i in range(3):
    verificacao.append(int(input()))

verificacao.remove(max(verificacao))
verificacao.remove(min(verificacao))
valor = verificacao[0]

if(valor >= 5 and valor <= 100):
    print(valor)