"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 13:27:11
"""


def organizar_pontuacoes(pontuacoes):
    p2 = []
    lista_p = []
    iterador = iter(pontuacoes)
    while True:
        try:
            p = iterador.__next__()
        except StopIteration:
            break
        else:
            while True:
                if len(lista_p) == 0:
                    lista_p.append(p)
                    pode_ir = True
                else:
                    if lista_p[-1][0] == p[0]:
                        lista_p.append(p)
                        pode_ir = True
                    else:
                        p2.append(lista_p.copy())
                        lista_p.clear()
                        pode_ir = False
                if pode_ir:
                    try:
                        p = iterador.__next__()
                    except StopIteration:
                        p2.append(lista_p.copy())
                        break
    return p2


def solve_this_problem():
    linha2 = set(linha)
    pontuacoes = []
    for char in linha2:
        pontuacoes.append((linha.count(char), ord(char)))
    pontuacoes.sort()
    pontuacoes2 = organizar_pontuacoes(pontuacoes)
    for pontuacoes in pontuacoes2:
        for pontuacoes2 in sorted(pontuacoes, reverse=True):
            print(pontuacoes2[1], pontuacoes2[0])


cont = 0
while True:
    try:
        linha = input()
    except EOFError:
        break
    else:
        if cont != 0:
            print()
        solve_this_problem()
        cont += 1
