# 100/100

entrada = list(map(float, input().split()))
media = sum(entrada)/2

if media >= 7: print("Aprovado")
elif media < 7 and media >= 4: print("Recuperacao")
else: print("Reprovado")
