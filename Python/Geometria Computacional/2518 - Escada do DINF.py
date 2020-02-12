"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 00:52:00
"""
while True:
    try:
        numero_degraus = int(input())
    except EOFError:
        break
    else:
        h, c, l = map(int, input().split())
        area_unitaria = ((h ** 2 + c ** 2) ** 0.5) * l
        area = area_unitaria * numero_degraus
        print('{:.4f}'.format(area/10000))
