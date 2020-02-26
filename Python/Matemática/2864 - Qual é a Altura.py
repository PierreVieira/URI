"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 00:26:53
"""
for i in range(int(input())):
    a, b, c = map(int, input().split())
    delta = b**2 - 4*a*c
    y_vertice = -(delta/(4*a))
    print('{:.2f}'.format(y_vertice))
