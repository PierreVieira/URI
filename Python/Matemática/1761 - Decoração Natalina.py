"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 23:08:50
"""
from math import tan
while True:
    try:
        a, b, c = map(float, input().split())
    except EOFError:
        break
    else:
        t = 5 * ((tan(a * (3.141592654/180)) * b) + c)
        print('{:.2f}'.format(t))
