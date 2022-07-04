# 100/100

n, copos = int(input()), 0

for i in range(n):
    lata, copo = map(int, input().split())
    if lata > copo:
        copos += copo

print(copos)