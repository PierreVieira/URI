"""
Autor: Pierre Vieira
Data da submissão: 08/02/2020 21:23:12
"""


def solve_this_problem():
    lista = [0 for c in range(257)]  # 257 contempla todas os ascii
    for i in range(len(palavra)):
        lista[ord(palavra[i])] += 1
    impar = 0
    for i in range(257):
        if lista[i] % 2 == 1:
            impar += 1
    if impar <= 1:
        return 0
    return impar - 1


while True:
    try:
        palavra = input()
    except EOFError:
        break
    else:
        print(solve_this_problem())
