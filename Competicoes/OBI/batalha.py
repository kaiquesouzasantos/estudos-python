# 100/100

a1 = int(input())
d1 = int(input())
a2 = int(input())
d2 = int(input())

if(a1 != d2 and d1 == a2):
    print("1\n")
elif(a2 != d1 and d2 == a1):
    print("2\n")
else:
    print("-1\n")