"""
Autor: Pierre Vieira
Data da submissão: 17/01/2020 21:16:51
"""

n = int(input())
lista_pontuacoes = [int(input()) for c in range(n)]
if lista_pontuacoes[0] < max(lista_pontuacoes):
    print('N')
else:
    print('S')
