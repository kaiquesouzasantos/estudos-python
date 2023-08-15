def contar_restricoes_violadas(grupos, pares_mesmo_grupo, pares_diferente_grupo):
    violacoes = 0

    # Crie um dicionário que mapeia os alunos aos seus grupos.
    grupos_por_aluno = {}
    for grupo in grupos:
        for aluno in grupo:
            grupos_por_aluno[aluno] = grupo

    # Percorra os pares de alunos que gostariam de estar no mesmo grupo.
    for par in pares_mesmo_grupo:
        aluno1, aluno2 = par

        # Verifique se os alunos estão no mesmo grupo.
        if grupos_por_aluno[aluno1] != grupos_por_aluno[aluno2]:
            violacoes += 1

    # Percorra os pares de alunos que não gostariam de estar no mesmo grupo.
    for par in pares_diferente_grupo:
        aluno1, aluno2 = par

        # Verifique se os alunos estão no mesmo grupo.
        if grupos_por_aluno[aluno1] == grupos_por_aluno[aluno2]:
            violacoes += 1

    return violacoes

E, M, D = map(int, input().split())
pares_mesmo_grupo = [list(map(int, input().split())) for _ in range(M)]
pares_diferente_grupo = [list(map(int, input().split())) for _ in range(D)]
    
grupos = [list(map(int, input().split())) for _ in range(E // 3)]
    
violacoes = contar_restricoes_violadas(grupos, pares_mesmo_grupo, pares_diferente_grupo)
print(violacoes)