"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 22:32:46
"""


def tabuada_so_um(a):
    for c in range(5, 11):
        print('{} x {} = {}'.format(a, c, a * c))


def tabuada_de_dois(a, b):
    for c in range(5, 11):
        print('{} x {} = {}'.format(a, c, a * c), end=' && ')
        print('{} x {} = {}'.format(b, c, b * c))


n = int(input())
for c in range(n):
    a, b = map(int, input().split('x'))
    if a == b:
        tabuada_so_um(a)
    else:
        tabuada_de_dois(a, b)
