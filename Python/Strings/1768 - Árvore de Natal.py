"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 15:31:26
"""


def printa_arvore():
    t = int(n/2 + 1)
    for asterisco in reversed(arvore2):
        print(' '*(n-t), end=asterisco)
        t += 1
        print()
    for asterisco in reversed(arvore):
        print(asterisco)


def solve_this_problem():
    for c in range(n, 0, -2):
        arvore2.append('*'*c)
    printa_arvore()


while True:
    try:
        n = int(input())
        arvore = [' '*((n//2) - 1)+'***', ' '*(n//2)+'*']
        arvore2 = []
    except EOFError:
        break
    else:
        solve_this_problem()
        print()
