# 100/100

def somac(figura, naipe) -> int:
    valor = 0
    global naipeD
    np = naipeD

    if(figura == "A"):
        if(np == naipe):valor = 14
        else: valor = 10
    elif(figura == "J"):
        if(np == naipe): valor = 15
        else:valor = 11
    elif(figura == "Q"):
        if(np == naipe):valor = 16
        else:valor = 12
    elif(figura == "K"):
        if(np == naipe): valor = 17
        else:valor = 13
    return valor

def soma(figura1, naipe1, figura2, naipe2, figura3, naipe3):
    return somac(figura1, naipe1) + somac(figura2, naipe2) + somac(figura3, naipe3)

l1 = input()
figura = l1[0]
naipeD = l1[1]

l2 = list(input()+" ")
l3 = list(input()+" ")
l4 = list(input()+" ")

l5 = list(input()+" ")
l6 = list(input()+" ")
l7 = list(input()+" ")

if(soma(l2[0], l2[1], l3[0], l3[1], l4[0], l4[1]) > soma(l5[0], l5[1], l6[0], l6[1], l7[0], l7[1])):
    print("Luana")
elif(soma(l2[0], l2[1], l3[0], l3[1], l4[0], l4[1]) < soma(l5[0], l5[1], l6[0], l6[1], l7[0], l7[1])):
    print("Edu")
else:
    print("empate")




