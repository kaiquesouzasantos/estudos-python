def verifica(str):
    maior = 1

    for i in range(len(str)):
        for j in range(i, len(str), 1):
            periodo = 1

            for k in range((j - i + 1) // 2):
                if (str[i + k] != str[j - k]):
                    periodo = 0

            if (periodo != 0 and
                    (j - i + 1) > maior):
                maior = j - i + 1
    return maior

n = int(input())
entrada = input()
print(verifica(entrada))