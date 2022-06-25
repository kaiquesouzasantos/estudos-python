def verifica(lin):
    d = lin[0] + lin[1] + lin[2]
    a1 = (lin[3] + lin[4]) / 2
    a2 = (lin[5] + lin[6] + lin[7]) / 3
    soma = int(d + a1 + a2)

    if (soma >= 60):
        print(f"Aluno aprovado com nota: {soma}")
    else:
        print(f"Aluno reprovado com nota: {soma}")

while True:
    lin = list(map(int, input().split()))
    if lin[0] == 0: break

    verifica(lin)