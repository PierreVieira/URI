"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 21:10:24
"""

n = int(input())
carrinhos, bonecas = 0, 0
for c in range(n):
    pessoa = tuple(map(str, input().split()))[1]
    if pessoa == 'F':
        bonecas += 1
    else:
        carrinhos += 1
print('{} carrinhos\n{} bonecas'.format(carrinhos, bonecas))
