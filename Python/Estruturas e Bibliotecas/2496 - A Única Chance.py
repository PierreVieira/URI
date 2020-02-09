"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 17:42:58
"""


def solve_this_problem():
    ordenada = ''.join(list(sorted(string)))
    for c in range(tamanho_string):
        for d in range(c + 1, tamanho_string):
            lista_string = list(string)
            lista_string[c], lista_string[d] = lista_string[d], lista_string[c]
            teste_string = ''.join(lista_string)
            if teste_string == ordenada:
                return 'There are the chance.'
    return "There aren't the chance."


for c in range(int(input())):
    tamanho_string = int(input())
    string = input()
    print(solve_this_problem())
