"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 21:17:04
"""


def arvore_boa(h, d, g):
    if 200 <= h <= 300 and d >= 50 and g >= 150:
        return 'Sim'
    return 'Nao'


n = int(input())
for c in range(n):
    h, d, g = map(int, input().split())
    print(arvore_boa(h, d, g))
