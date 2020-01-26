"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 20:03:57
"""


def caminhadas(char1, char2):
    """
    Calcula o tanto que tenho que andar para que char1 == char2
    """
    qtde_andadas = 0
    letras = 'abcdefghijklmnopqrstuvwxyz'
    while char1 != char2:
        posicao = letras.index(char1) + 1
        if posicao == 26:
            posicao = 0
        char1 = letras[posicao]
        qtde_andadas += 1
    return qtde_andadas


def qtde_trocas_necessarias(string1, string2):
    cont = 0
    for c in range(len(string1)):
        cont += caminhadas(string1[c], string2[c])
    return cont


for c in range(int(input())):
    string1, string2 = map(str, input().split())
    print(qtde_trocas_necessarias(string1, string2))
