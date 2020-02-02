"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 16:27:06
"""


def solve_this_problem():
    lista_desejada = list('COBOL')
    lista_reversa = list(reversed(lista_desejada))
    for palavra in palavras:
        if not (palavra[0].upper() == lista_reversa[-1] or palavra[-1].upper() == lista_reversa[-1]):
            return 'BUG'
        else:
            lista_reversa.pop()
    return 'GRACE HOPPER'


while True:
    try:
        palavras = input().split('-')
    except EOFError:
        break
    else:
        print(solve_this_problem())
