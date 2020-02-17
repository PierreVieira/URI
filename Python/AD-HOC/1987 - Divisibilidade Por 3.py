"""
Autor: Pierre Vieira
Data da submissão: 16/02/2020 22:51:43
"""


def divisivel_por_3():
    cont = 0
    for s in n:
        cont += int(s)
    if cont % 3 == 0:
        return cont, 'sim'
    return cont, 'nao'


while True:
    try:
        linha = input()
    except EOFError:
        break
    else:
        tam_n, n = linha.split()
        retorno = divisivel_por_3()
        print('{} {}'.format(retorno[0], retorno[1]))
