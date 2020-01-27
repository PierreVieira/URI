"""
Autor: Pierre Vieira
Data da submissão: 27/01/2020 13:40:07
"""


def solve_this_problem(entrada):
    caminho = 'NLSO'
    cont = 0
    for c in range(len(entrada)):
        if entrada[c] == 'D':
            cont += 1
            if cont == 4:
                cont = 0
        else:
            cont -= 1
            if cont == -1:
                cont = 3
    print(caminho[cont])


while True:
    n = int(input())
    if n == 0:
        break
    solve_this_problem(input())
