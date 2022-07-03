# 100/100

def verifica(exp) -> str:
    if exp in "-*#10": return exp
    elif exp in "ABC": return "2"
    elif exp in "DEF": return "3"
    elif exp in "GHI": return "4"
    elif exp in "JKL": return "5"
    elif exp in "MNO": return "6"
    elif exp in "PQRS": return "7"
    elif exp in "TUV": return "8"
    elif exp in "WXYZ":return "9"

entrada, saida = input(), ""

for i in entrada:
    saida += verifica(i)

print(saida)
