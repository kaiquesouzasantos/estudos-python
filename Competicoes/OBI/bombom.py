# 100/100

def somac(figura, naipe):
    global naipeD
    np = naipeD

    if(np == naipe):
        figuras = {'A':14,'J':15,'Q':16,'K':17}
        return figuras[figura]
    else:
        figuras = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}
        return figuras[figura]

def soma(figura1, naipe1, figura2, naipe2, figura3, naipe3):
    return somac(figura1, naipe1) + somac(figura2, naipe2) + somac(figura3, naipe3)

l1 = input()
figura = l1[0]
naipeD = l1[1]

l2, l3, l4 = input(), input(), input()
l5, l6, l7 = input(), input(), input()

soma1 = soma(l2[0], l2[1], l3[0], l3[1], l4[0], l4[1])
soma2 = soma(l5[0], l5[1], l6[0], l6[1], l7[0], l7[1])

if(soma1 > soma2):print("Luana")
elif(soma1 < soma2): print("Edu")
else: print("empate")
