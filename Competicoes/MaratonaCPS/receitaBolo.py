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

print("1 Milho verde "+str(milho)+"KG")
print("2 Oleo vegetal "+str(oleo)+"L")
print("3 Acucar "+str(acucar)+"KG")
print("4 Fuba "+str(fuba)+"KG")
print("5 Ovos "+str(ovo))
print("6 Farinha de trigo "+str(farinha)+"KG")
print("7 Coco ralado "+str(coco)+"KG")
print("8 Fermento em po "+str(fermento)+"KG")
print("9 Leite de coco "+str(leiteC)+"L")
print("10 Chocolate em po "+str(choc)+"KG")
print("11 Leite "+str(leite)+"L")
