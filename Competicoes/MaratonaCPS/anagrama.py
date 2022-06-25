def comparar(dig, pal):
    if len(dig) > len(pal): return False
    
    cont = 0
    temp = []

    for x in range(len(pal)):
        temp.append(pal[x]) # temp = full split da 1° palavra
        
    for x in range(len(dig)):
        for i in range(len(temp)):
            if dig[x] == temp[i]: # letraDig esta contida em temp?
                cont += 1
                temp[i] = "-" # modifca temp
                break
    return cont == len(dig)

while True:
    linha = input()

    if linha in '0': break

    temp = linha.split(" ")
    n = 0

    for x in range(1,len(temp)):
        if comparar(temp[x], temp[0]):
            n += 1
    print(n)