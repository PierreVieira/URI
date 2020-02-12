"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 19:58:35
"""


def solve_this_problem(dolares, centavos):
    if len(centavos) < 2:
        centavos = '0'+centavos
    s = ''
    cont = 0
    for d in reversed(dolares):
        s += d
        cont += 1
        if cont == 3:
            s += ','
            cont = 0
    s = ''.join(reversed(s))+'.'
    s += centavos
    if s[0] == ',':
        print('$'+s[1:])
    else:
        print('$'+s)


def main():
    while True:
        try:
            dolares = int(input())
        except EOFError:
            break
        else:
            centavos = int(input())
            solve_this_problem(str(dolares), str(centavos))


main()
