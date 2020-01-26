"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 16:46:24
"""


def solve_this_problem():
    qtde_pares_possiveis = 0
    visitados = []
    for c in range(n):
        tam_busca = lista_calcados[c][0]
        if not (tam_busca in visitados):
            visitados.append(tam_busca)
            qtde_direitos = lista_calcados.count([tam_busca, 'D'])
            qtde_esquerdos = lista_calcados.count([tam_busca, 'E'])
            qtde_pares_possiveis += min(qtde_esquerdos, qtde_direitos)
    return qtde_pares_possiveis


while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        lista_calcados = [input().split() for c in range(n)]
        print(solve_this_problem())
