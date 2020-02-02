"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 14:08:21
"""
for c in range(int(input())):
    n = int(input())
    qtde_graos = 2**n
    qtde_gramas = qtde_graos/12
    quilos = qtde_gramas/1000
    print('{} kg'.format(int(quilos)))