
numero = int(input())
s, resposta = input(), 0

for letra in range(numero):
    for r in range(letra, numero):
        eh_palindromo = True
        pl, pr = letra, r

        while pl <= pr:
            if s[pl] != s[pr]:
                eh_palindromo = False

            pl = pl + 1
            pr = pr - 1

        if eh_palindromo:
            resposta = max(resposta, r - letra + 1)

print(resposta)