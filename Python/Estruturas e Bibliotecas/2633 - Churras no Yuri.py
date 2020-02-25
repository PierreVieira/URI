"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 21:12:37
"""


def solve_this_problem():
    lista = []
    for c in range(n):
        nome, num = input().split()
        lista.append((int(num), nome))
    lista.sort()
    for c in range(n - 1):
        print(lista[c][1], end=' ')
    print(lista[n - 1][1])


while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        solve_this_problem()
