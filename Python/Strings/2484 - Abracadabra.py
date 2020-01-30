"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 15:17:04
"""


def printar_string(s):
    tamanho = len(s)
    count = 0
    t = tamanho
    for string in range(int(tamanho/2 + 1)):
        print('{}{}'.format(' '*(tamanho - t), s[0:tamanho - count]))
        count += 2
        t -= 1


def solve_this_problem():
    s = ''
    for c in range(len(entrada) - 1):
        s += entrada[c]
        s += ' '
    s += entrada[len(entrada) - 1]
    printar_string(s)


while True:
    try:
        entrada = input()
    except EOFError:
        break
    else:
        solve_this_problem()
        print()
