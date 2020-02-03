"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 21:26:33
"""


def gerar_colunas(a, b, matriz):
    colunas = []
    for col in range(a):
        coluna = []
        for lin in range(b):
            coluna.append(matriz[lin][col])
        colunas.append(coluna.copy())
    return colunas


def solve_this_problem(colunas, tam_coluna):
    for coluna in colunas:
        if sum(coluna) == tam_coluna:
            return 'yes'
    return 'no'


def main():
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        matriz = [tuple(map(int, input().split())) for c in range(b)]
        colunas = gerar_colunas(a, b, matriz)
        print(solve_this_problem(colunas, b))


main()
