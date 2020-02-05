"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 17:11:16
"""
from math import ceil

for c in range(int(input())):
    qtde_linhas, qtde_colunas = map(int, input().split())
    print(ceil((qtde_linhas-2)/3) * ceil((qtde_colunas-2)/3))
