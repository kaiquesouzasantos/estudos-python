# 100/100

cV, cE, cG, fV, fE, fG = map(int, input().split())
cPontos = cE + (3 * cV)
fPontos = fE + (3 * fV)

if (cPontos > fPontos) or ((cPontos == fPontos) and (cG > fG)): print("C")
elif (cPontos < fPontos) or ((cPontos == fPontos) and (cG < fG)): print("F")
else: print("=")