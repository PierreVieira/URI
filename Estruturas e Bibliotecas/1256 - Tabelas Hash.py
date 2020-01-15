"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 20:02:38
"""


def printa_posicao_da_tabela(values):
    for valor in values:
        print(valor, end=' -> ')
    print(chr(92))


def printa_tabela_hash():
    for index in range(len(lista_posicoes)):
        print('{}'.format(index), end=' -> ')
        printa_posicao_da_tabela(lista_posicoes[index])


def tabela_hash(valores):
    for valor in valores:
        posicao = valor % tam
        lista_posicoes[posicao].append(valor)


n = int(input())
for c in range(n):
    tam, qtde_valores = map(int, input().split())
    lista_posicoes = [[] for d in range(tam)]
    valores = list(map(int, input().split()))
    tabela_hash(valores)
    printa_tabela_hash()
    if c < n-1:
        print()
