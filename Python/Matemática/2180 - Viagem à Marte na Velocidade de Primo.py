"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 22:56:06
"""


def primo(x):
    qtde_div = 0
    for c in range(2, int(x ** 0.5) + 1):
        if x % c == 0:
            qtde_div += 1
    if qtde_div != 0:
        return False
    return True


def encontra_lista_primos(inicio):
    lista = []
    while len(lista) != 10:
        if primo(inicio):
            lista.append(inicio)
        inicio += 1
    return lista


soma_primos = sum(encontra_lista_primos(int(input())))
qtde_horas = (60*10**6)/soma_primos
qtde_dias = qtde_horas / 24
print('{} km/h\n{} h / {} d'.format(soma_primos, int(qtde_horas), int(qtde_dias)))
