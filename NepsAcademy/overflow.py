# 100/100

limite, verifica = int(input()), 0
num1, c, num2 = input().split()

if c == "*": verifica = int(num1) * int(num2)
else: verifica = int(num1) + int(num2)

if verifica > limite: print("OVERFLOW")
else: print("OK")
