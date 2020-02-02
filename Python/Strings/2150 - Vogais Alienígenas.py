"""
Autor: Pierre Vieira
Data da submissão: 31/01/2020 22:42:27
"""


def solve_this_problem():
    cont = 0
    for caractere in vogais:
        cont += frase.count(caractere)
    print(cont)


while True:
    try:
        vogais, frase = input(), input()
    except EOFError:
        break
    else:
        solve_this_problem()
