"""
Autor: Pierre Vieira
Data da submissão: 16/02/2020 16:03:28
"""
from itertools import combinations


def forma_prasodia():
    for i in range(n, 1, -1):
        for combinacao in combinations(cartas, i):
            x = y = z = 0
            for tupla in combinacao:
                x += tupla[0]
                y += tupla[1]
                z += tupla[2]
            if x == a and y == d and z == h:
                return True
    return False


n, a, d, h = map(int, input().split())
cartas = [list(map(int, input().split())) for c in range(n)]
if forma_prasodia():
    print('Y')
else:
    print('N')