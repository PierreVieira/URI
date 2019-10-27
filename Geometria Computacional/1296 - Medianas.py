"""
Autor: Pierre Vieira
Data da submissão: 03/02/2019 23:01:32
"""
from math import sqrt
while True:
    try:
        linha = input().split()
        mediana1, mediana2, mediana3 = list(map(float, linha))
        if mediana1 >= mediana3 + mediana2 or mediana2 >= mediana1 + mediana3 or mediana3 >= mediana1 + mediana2:
            print('-1.000')
        else:
            sp = (mediana1+mediana2+mediana3)/2
            area_pequena = sqrt(sp*(sp - mediana1)*(sp - mediana2)*(sp - mediana3))
            area = (4/3)*area_pequena
            print("{:.3f}".format(area))
    except EOFError:
        break