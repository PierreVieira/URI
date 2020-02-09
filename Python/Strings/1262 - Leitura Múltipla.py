"""
Autor: Pierre Vieira
Data da submissão: 08/02/2020 21:05:44
"""


def solve_this_problem():
    string = ''
    cont = 0
    for s in rastro:
        if s == 'W':
            if len(string) > 0:
                cont += 1
            cont += 1
            string = ''
        else:
            string += s
            if p == len(string):
                cont += 1
                string = ''
    if len(string) > 0:
        cont += 1
    return cont


while True:
    try:
        rastro = input()
    except EOFError:
        break
    else:
        p = int(input())
        print(solve_this_problem())