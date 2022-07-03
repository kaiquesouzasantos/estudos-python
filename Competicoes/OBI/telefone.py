def verifica(exp):
    if exp == "-": return "-"
    elif exp == "*": return "*"
    elif exp == "#": return "#"
    elif exp == "1": return "1"
    elif exp == "0": return "0"
    elif exp == "A" or exp == "B" or exp == "C": return "2"
    elif exp == "D" or exp == "E" or exp == "F": return "3"
    elif exp == "G" or exp == "H" or exp == "I": return "4"
    elif exp == "J" or exp == "K" or exp == "L": return "5"
    elif exp == "M" or exp == "N" or exp == "O": return "6"
    elif exp == "P" or exp == "Q" or exp == "R" or exp == "S": return "7"
    elif exp == "T" or exp == "U" or exp == "V": return "8"
    elif exp == "W" or exp == "X" or exp == "Y" or exp == "Z": return "9"

entrada, saida = input(), ""

for i in entrada:
    saida += verifica(i)
print(saida)