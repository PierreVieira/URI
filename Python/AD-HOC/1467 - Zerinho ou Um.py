"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 15:28:10
"""


def solve_this_problem():
    if a == b == c:
        return '*'
    elif a == c and a != b:
        return 'B'
    elif a == b and a != c:
        return 'C'
    else:
        return 'A'


while True:
    try:
        a, b, c = map(int, input().split())
    except EOFError:
        break
    else:
        print(solve_this_problem())