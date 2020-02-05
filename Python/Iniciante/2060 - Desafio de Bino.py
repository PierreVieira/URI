"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 17:59:36
"""


def multiplo_de(lista, n):
    cont = 0
    for num in lista:
        if num % n == 0:
            cont += 1
    return cont


def main():
    n = int(input())
    lista = list(map(int, input().split()))
    for c in range(2, 6):
        print('{} Multiplo(s) de {}'.format(multiplo_de(lista, c), c))


main()