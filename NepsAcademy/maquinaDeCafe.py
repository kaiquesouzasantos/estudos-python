# 100/100

a, b, c = int(input()), int(input()), int(input())

"""
-> 10, 20, 30
10: (20*2) + (30*4) = 160 minutos
20: (10*2) + (30*2) = 80 minutos
30: (10*4) + (20*2) = 80 minutos
"""

andares = [
    ((2*b) + (4*c)),
    ((2*a) + (2*c)),
    ((2*b) + (4*a))
]

print(min(andares))
