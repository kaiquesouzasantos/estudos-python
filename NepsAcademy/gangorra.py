# 100/100

p1, c1, p2, c2 = list(map(int, input().split()))

if (p1*c1) > (p2*c2): print(-1)
elif (p1*c1) < (p2*c2): print(1)
else: print(0)