"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 19:03:06
"""


def qtde_nao_trocados(lista, ordenada):
    cont = 0
    for d in range(len(lista)):
        if lista[d] == ordenada[d]:
            cont += 1
    return cont


n = int(input())
for c in range(n):
    m = int(input())
    lista = list(map(int, input().split()))
    ordenada = sorted(lista, reverse=True)
    print(qtde_nao_trocados(lista, ordenada))
