# 100/100

colchao = list(map(int, input().split()))
porta = list(map(int, input().split()))

colchao.sort(), porta.sort()

# testa a possibilidade utilizando os menores valores
if (colchao[0] <= porta[0]) and (colchao[1] <= porta[1]): print("S")
else: print("N")