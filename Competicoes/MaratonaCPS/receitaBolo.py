milho, oleo, acucar, fuba, ovo, farinha, coco, fermento, leiteC, leite, choc = 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0 ,0

def boloMilho(qtd):
    global milho, oleo,acucar, fuba, ovo, farinha, coco, fermento
    milho += qtd * 0.2
    oleo += qtd * 0.2
    acucar += qtd * 0.26
    fuba += 0.2
    ovo += qtd * 4
    farinha += qtd * 0.015
    coco += qtd * 0.015
    fermento += qtd * 0.005

def boloCoco(qtd):
    global oleo, acucar, ovo, farinha, coco, fermento, leiteC
    oleo += qtd * 0.12
    acucar += qtd * 0.36
    ovo += qtd * 4
    farinha += qtd * 0.24
    coco += qtd * 0.1
    fermento += qtd * 0.01
    leiteC += qtd * 0.2

def boloChoc(qtd):
    global oleo, acucar, ovo, farinha, coco, fermento, choc, leite
    oleo += qtd * 0.24
    acucar += qtd * 0.16
    ovo += qtd * 2
    farinha += qtd * 0.24
    fermento += qtd * 0.015
    choc += qtd * 0.09
    leite += qtd * 0.24

dias = int(input())

for i in range(dias):
    lin = list(map(int, input().split()))
    boloMilho(lin[0]), boloCoco(lin[1]), boloChoc(lin[2])

print(f"1 Milho verde {milho} KG")
print(f"2 Oleo vegetal {oleo}L")
print(f"3 Açucar {acucar}KG")
print(f"4 Fuba {fuba}KG")
print(f"5 Ovos {ovo}")
print(f"6 Farinha de trigo {farinha}KG")
print(f"7 Coco ralado {coco}KG")
print(f"8 Fermento em po {fermento}KG")
print(f"9 Leite de coco {leiteC}L")
print(f"10 Chocolate em po {choc}KG")
print(f"11 Leite {leite}L")