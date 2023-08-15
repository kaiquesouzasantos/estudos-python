def maior_intervalo_distinto(sequencia):
    max_intervalo = 0
    seen = set()  # Conjunto para rastrear elementos únicos
    left = 0  # Índice esquerdo do intervalo
    
    for right in range(len(sequencia)):
        while sequencia[right] in seen:
            seen.remove(sequencia[left])
            left += 1
        seen.add(sequencia[right])
        max_intervalo = max(max_intervalo, right - left + 1)
    
    return max_intervalo

N = int(input())
sequencia = [int(input()) for _ in range(N)]
resultado = maior_intervalo_distinto(sequencia)
print(resultado)
