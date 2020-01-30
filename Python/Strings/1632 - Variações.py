"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 15:39:47
"""


def resultado(lista_possibilidades):
    result = 1
    for c in lista_possibilidades:
        result *= c
    return result


def numero_variacoes(string):
    lista_possibilidades = []
    for char in string:
        if char.upper() in 'AEIOS':
            lista_possibilidades.append(3)
        else:
            lista_possibilidades.append(2)
    return resultado(lista_possibilidades)


def main():
    for c in range(int(input())):
        string = input()
        print(numero_variacoes(string))


main()
