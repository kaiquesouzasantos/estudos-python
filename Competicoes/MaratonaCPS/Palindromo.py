import sys

def decToBin(decNum):
    bin = ""
    while decNum > 0:
        resto = decNum % 2
        decNum = int(decNum/2)
        bin = bin + str(resto)

    return bin

if __name__ == "__main__":
    while True:            
        linha = input()
        
        if linha in '0': break

        n = int(linha)

        bin = decToBin(n)

        pal = True
        tam = len(bin)

        for x in range(tam):
            if not bin == bin[::-1]:
                pal = False
                break

        if pal:
            print("V")
        else:
            print("F")
            
sys.exit()