con = int(input())
nomes = []

for i in range(con):
	nomes.append(input())

nomes.sort()

for i, nome in enumerate(nomes):
	if i != len(nomes) - 1:
		print(f"Bem-vindo(a), {nome}!!!", end="")
	else:
		print(f"Bem-vindo(a), {nome}!!!", end="")