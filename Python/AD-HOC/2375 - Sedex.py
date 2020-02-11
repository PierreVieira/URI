"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 00:46:53
"""
from math import pi

diametro = int(input())
raio = diametro/2
a, b, c = map(int, input().split())
volume = (4/3)*pi*raio**3
if diametro > a or diametro > b or diametro > c:
    print('N')
elif volume <= a*b*c:
    print('S')
else:
    print('N')
