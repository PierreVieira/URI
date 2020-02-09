"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 16:55:10
"""


def preenche_diagonal_pricipal():
    matriz[0][0] = 1
    for c in range(1, n):
        matriz[c][c] = matriz[c - 1][c - 1] * 4


def preenche_abaixo_da_diagonal_principal():
    for d in range(n):
        for c in range(d + 1, n):
            matriz[c][d] = matriz[c - 1][d] * 2


def espelha_matriz_para_cima():
    for c in range(n):
        for d in range(c + 1, n):
            matriz[c][d] = matriz[d][c]


def printar_matriz(max_qtde_alg):
    for c in range(n):
        for d in range(n):
            print(' ' * (max_qtde_alg - len(str(matriz[c][d]))) + str(matriz[c][d]), end='')
            if d != n - 1:
                print(' ', end='')
        print()


def solve_this_problem():
    preenche_diagonal_pricipal()
    preenche_abaixo_da_diagonal_principal()
    espelha_matriz_para_cima()
    max_qtde_alg = len(str(matriz[-1][-1]))
    printar_matriz(max_qtde_alg)


while True:
    n = int(input())
    if n == 0:
        break
    matriz = [[0 for d in range(n)] for c in range(n)]
    solve_this_problem()
    print()
