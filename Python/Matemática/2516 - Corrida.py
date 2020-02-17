"""
Autor: Pierre Vieira
Data da submissão: 16/02/2020 19:55:07
"""


def solve_this_problem():
    # S = So + v*t
    t = -s/(vb - va)
    if t < 0:
        return 'impossivel'
    return '{:.2f}'.format(t)


while True:
    try:
        s, va, vb = map(int, input().split())
    except EOFError:
        break
    else:
        print(solve_this_problem())
