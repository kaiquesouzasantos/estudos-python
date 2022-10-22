import sys

if __name__ == "__main__":
    while True:            
        linha = input()
        if linha in '0': break

        n = int(linha)

        binario = bin(n)

        pal = True
        tam = len(binario)

        for x in range(tam):
            if not binario == binario[::-1]:
                pal = False
                break

        if pal: print("V")
        else: print("F")
            
sys.exit()
