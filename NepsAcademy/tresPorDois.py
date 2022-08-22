# 100/100

N = int(input())
chocolates = list()

for i in range(N):
    chocolates.append(int(input()))
chocolates.sort()

print(sum(chocolates[N//3:]))