"""
Autor: Pierre Vieira
Data da submissão: 27/01/2020 14:32:55
"""


def solve_this_problem(risada_vogais):
    if risada_vogais == list(reversed(risada_vogais)):
        return 'S'
    return 'N'


risada = input()
apenas_vogais = [c for c in risada if c in 'aeiou']
print(solve_this_problem(apenas_vogais))
