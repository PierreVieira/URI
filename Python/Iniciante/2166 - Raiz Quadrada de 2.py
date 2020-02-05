"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 18:31:16
"""


def metodo_fracoes_continuas(tolerancia, n=2):
    x = 0
    for c in range(tolerancia):
        x += n
        x = 1 / x
    x += 1
    return x


print('{:.10f}'.format(metodo_fracoes_continuas(int(input()))))
