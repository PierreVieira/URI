"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 13:06:48
"""
from math import pow
for c in range(int(input())):
    a, b = map(int, input().split())
    if a == b == 0:
        print(0)
    else:
        c1, c2 = pow(26, a), pow(10, b)
        print(int(c1*c2))
