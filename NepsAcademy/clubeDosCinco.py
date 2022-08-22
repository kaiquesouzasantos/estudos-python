# 100/100

assoc = int(input())
a, b, c, d, e, f, g = map(int, input().split())

"""
a | b | c | g -> falaram a verdade, então sua soma corresponde ao numero de associados
d | e | f -> mentiram, pois não estão necessariamente praticando dois/+ esportes

-> a soma dos valores verdadeiros, sendo subtraido os valores falsos resulta no numero de associados
"""

if assoc == (a + b + c + g - d - e - f):
    print("N")
else:
    print("S")