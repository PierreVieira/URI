"""
Autor: Pierre Vieira
Data da submissão: 18/02/2020 08:25:31
"""


def solve_this_problem():
    soma_linha = sum(linha)
    if soma_linha % n != 0:
        return -1
    soma_linha /= n
    maior = 1
    for c in range(n):
        if linha[c] > soma_linha:
            maior += linha[c] - soma_linha
    return int(maior)


while True:
    try:
        n = int(input())
        linha = tuple(map(int, input().split()))
    except EOFError:
        break
    else:
        print(solve_this_problem())
