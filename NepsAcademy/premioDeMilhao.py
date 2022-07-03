# 100/100

n, soma, dias = int(input()), 0, 0

for i in range(n):
    soma += int(input())
    dias += 1

    if soma >= 1000000: break

print(dias)
