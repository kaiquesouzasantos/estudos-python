# 100/100

largura = int(input())
comprimento = int(input())

if(largura > 0 and comprimento > 0 and largura <= 100 and comprimento <= 100):
    print((largura*comprimento) + (largura-1)*(comprimento-1))  
    print(2*(largura-1) + 2*(comprimento-1))
else:
    exit()