"""
Autor: Pierre Vieira
Data da submissão: 31/01/2020 19:44:18
"""


def gerar_m():
    """O tamanho da lista m será o tamanho da stirng"""
    lista = []
    for c in range(1, len(matring[0]) - 1):
        string = ''
        for tupla in matring:
            string += tupla[c]
        lista.append(int(string))
    return lista


def string_formada():
    string = ''
    for c in range(tamanho_string):
        string += chr((f * m[c] + l) % 257)
    return string


matring = [tuple((input())) for c in range(4)]
tamanho_string = len(matring[0]) - 2
f, l = int(''.join([tupla[0] for tupla in matring])), int(''.join([tupla[-1] for tupla in matring])) # f e l são, respectivamente a primeira e ultima coluna
m = gerar_m()
print(string_formada())
