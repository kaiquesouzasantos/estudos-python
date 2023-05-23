# 100/100

feliz, triste = ':-)', ':-('
leitura = input()

if(leitura.count(feliz) > leitura.count(triste)):
    print('divertido')
elif(leitura.count(feliz) < leitura.count(triste)):
    print('chateado')
else:
    print('neutro')