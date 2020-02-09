"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 17:10:47
"""


def soma_notas_compasso(compasso):
    soma = 0
    for nota in compasso:
        if nota == 'W':
            soma += 1
        elif nota == 'H':
            soma += 0.5
        elif nota == 'Q':
            soma += 0.25
        elif nota == 'E':
            soma += 0.125
        elif nota == 'S':
            soma += 0.0625
        elif nota == 'T':
            soma += 0.03125
        else:
            soma += 0.015625
    return soma


def compasso_ok(compasso):
    return soma_notas_compasso(compasso) == 1


def solve_this_problem():
    cont = 0
    for compasso in compassos:
        if compasso_ok(compasso):
            cont += 1
    return cont


while True:
    composicao = input()
    if composicao == '*':
        break
    compassos = composicao.split('/')[1:-1]
    print(solve_this_problem())
