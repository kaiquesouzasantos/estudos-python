# 100/100

hAtual, mAtual, hComeca, mComeca = int(input()), int(input()), int(input()), int(input())

# se (somaMinutosAtual + tempoChegada) <= (somaMinutosComeca) == momentoChegada <= inicioReuniao
if ((hAtual * 60) + mAtual + 45) <= ((hComeca * 60) + mComeca):
    print("Sucesso")
else:
    print(f"Atrasado {((hAtual * 60) + mAtual + 45) - ((hComeca * 60) + mComeca)}")
