# 100/100

x, y = int(input()), int(input())

if x > 0 and y > 0: print("Q1")
elif x < 0 and y > 0: print("Q2")
elif x < 0 and y < 0: print("Q3")
elif x == 0 or y == 0: print("eixos")
else: print("Q4")