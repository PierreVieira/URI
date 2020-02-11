"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 13:41:30
"""


def solve_this_problem():
    ja_adicionados = []
    cont = 0
    for num in lista_perguntas:
        if not num in ja_adicionados:
            if lista_perguntas.count(num) >= k:
                ja_adicionados.append(num)
                cont += 1
    return cont


while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    lista_perguntas = input().split()
    print(solve_this_problem())
