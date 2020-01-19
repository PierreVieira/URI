"""
Autor: Pierre Vieira
Data da submissão: 17/01/2020 20:46:59
"""


def duplo_n(n):
    # Eq de recorrência
    # D(0) = 1
    # D(1) = D(n-1) + (n+1)
    return (n ** 2 + 3 * n) / 2 + 1  # Fórmula fechada


print(int(duplo_n(int(input()))))
