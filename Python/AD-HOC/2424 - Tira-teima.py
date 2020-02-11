"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 17:31:32
"""
x, y = map(int, input().split())


def dentro_fora():
    if 0 <= x <= 432 and  0 <= y <= 468:
        return 'dentro'
    return 'fora'


print(dentro_fora())
