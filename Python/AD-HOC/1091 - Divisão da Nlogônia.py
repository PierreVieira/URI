"""
Autor: Pierre Vieira
Data da submissão: 29/01/2020 20:46:43
"""


def localizacao(x, y):
    if x > 0 and y > 0:
        return 'NE'
    elif x > 0 and y < 0:
        return 'SE'
    elif x < 0 and y < 0:
        return 'SO'
    elif x < 0 and y > 0:
        return 'NO'
    return 'divisa'


def solve_this_problem(x, y, n, m):
    # Ponto divisor = n, m
    # Mudando as coordenads para considerar que o centro é em 0, 0
    x -= n
    y -= m
    return localizacao(x, y)


while True:
    qtde_consultas = int(input())
    if qtde_consultas == 0:
        break
    n, m = map(int, input().split())  # Coordenadas do poto divisor
    for c in range(qtde_consultas):
        x, y = map(int, input().split())
        print(solve_this_problem(x, y, n, m))
