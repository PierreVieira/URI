"""
Autor: Pierre Vieira
Data da submissão: 16/01/2020 14:07:23
"""


def quantidade_sexo(numeros_sexo, n, sexo):
    cont = 0
    for elemento in numeros_sexo:
        if elemento[0] == n and elemento[1] == sexo:
            cont += 1
    return cont


def solve_this_problem(entrada, n):
    numeros = tuple(map(int, tuple(filter(lambda elemento: entrada.index(elemento) % 2 == 0, entrada))))
    sexo = tuple(filter(lambda elemento: entrada.index(elemento) % 2 == 1, entrada))
    numeros_sexo = tuple(zip(numeros, sexo))
    qtde_pares_iguais = numeros.count(n)
    qtde_feminino = quantidade_sexo(numeros_sexo, n, 'F')
    qtde_masculino = quantidade_sexo(numeros_sexo, n, 'M')
    print('Pares Iguais: {}\nF: {}\nM: {}'.format(qtde_pares_iguais, qtde_feminino, qtde_masculino))


def main():
    cont = 0
    while True:
        cont += 1
        try:
            n = int(input())
            lista = input().split()
            if cont > 1:
                print()
        except EOFError:
            break
        else:
            print('Caso {}:'.format(cont))
            solve_this_problem(lista, n)


main()
