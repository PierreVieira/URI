"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 13:23:08
"""


def qtde_picos(lista_analise):
    cont = 0
    for c in range(len(lista_analise)):
        if lista_analise[c] != lista_analise[c-1]:
            cont += 1
    return cont


def qtde_picos_existentes():
    sequencia2 = sequencia.copy()
    for c in range(1, len(sequencia)):
        sequencia[c], sequencia[c-1] = sequencia[c-1], sequencia[c]
    tupla_analise = tuple(zip(sequencia, sequencia2))
    lista_analise = []
    for elemento in tupla_analise:
        if elemento[0] > elemento[1]:
            lista_analise.append('Aumenta')
        else:
            lista_analise.append('Diminui')
    return qtde_picos(lista_analise)


while True:
    n = int(input())
    if n == 0:
        break
    sequencia = list(map(int, input().split()))
    print(qtde_picos_existentes())
