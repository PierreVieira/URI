"""
Autor: Pierre Vieira
Data da submissão: 02/03/2019 15:37:58
"""


def correct(lista):
    if lista.count('(') != lista.count(')'):
        return 'incorrect'
    if lista[0] == ')':
        return 'incorrect'
    if lista[-1] == '(':
        return 'incorrect'
    return 'correct'


while True:
    try:
        string = input().strip()
        lista = []
        for c in string:
            lista.append(c)
        print(correct(lista))
    except EOFError:
        break
