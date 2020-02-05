"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 17:50:26
"""


def qtde_divisores(n):
    cont = 0
    for c in range(1, n//2 + 1):
        if n % c == 0:
            cont += 1
    return cont


def only_even(pesquisa):
    if qtde_divisores(pesquisa) % 2 == 1:
        return True
    return False


lista_esferas = [i for i in range(1, 1001)]
for c in range(int(input())):
    numeros = tuple(filter(only_even, lista_esferas[:int(input())]))
    print(len(numeros))