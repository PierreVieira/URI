"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 18:43:55
"""


def find_numbers(expressao):
    numero = ''
    lista_numeros = []
    c = 0
    while c < len(expressao):
        try:
            while expressao[c] != '-' and expressao[c] != '+':
                numero += expressao[c]
                c += 1
        except IndexError:
            lista_numeros.append(int(numero))
            break
        c += 1
        lista_numeros.append(int(numero))
        numero = expressao[c-1]
    return lista_numeros


def main():
    cont = 0
    while True:
        cont += 1
        valores = int(input())
        if valores == 0:
            break
        expressao = input()
        if expressao[0] == '-':
            numeros = find_numbers(expressao)
        else:
            numeros = find_numbers(expressao)
        print('Teste {}'.format(cont))
        print(sum(numeros))
        print()


main()
