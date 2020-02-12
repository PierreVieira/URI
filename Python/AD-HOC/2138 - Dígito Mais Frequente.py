"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 17:34:39
"""


def posicao_left(aparicoes):
    maior = max(aparicoes)
    for c in range(9, -1, -1):
        if aparicoes[c] == maior:
            return c


def solve_this_problem():
    lista_digitos = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    aparicoes = [digitos.count(digito) for digito in lista_digitos]
    p = posicao_left(aparicoes)
    print(p)


while True:
    try:
        digitos = input()
    except EOFError:
        break
    else:
        solve_this_problem()
