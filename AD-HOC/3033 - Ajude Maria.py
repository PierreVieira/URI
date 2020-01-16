"""
Autor: Pierre Vieira
Data da submissão: 15/01/2020 22:55:10
"""

def mesma_linha(p1, p2):
    return p1[0] == p2[0]


def mesma_coluna(p1, p2):
    return p1[1] == p2[1]


def entre(p1, p, p2):
    if p1[0] <= p[0] <= p2[0] and p2[1] <= p[1] <= p1[1] or p1[0] <= p[0] <= p2[0] and p1[1] <= p[1] <= p2[1]:
        return True
    return False


def estao_ok(p1, p2, matriz):
    if mesma_linha(p1, p2) or mesma_coluna(p1, p2):
        return True
    for p in matriz:
        if p != p1 and p != p2:
            if entre(p1, p, p2) or entre(p2, p, p1):
                return True
    return False


def preenche_matriz(qtde_pontos):
    matriz = []
    for c in range(qtde_pontos):
        matriz.append(tuple(map(int, input().split())))
    return matriz


def solve_this_problem(matriz):
    for c in range(len(matriz)):
        for d in range(len(matriz)):
            if c != d:
                p1, p2 = matriz[c], matriz[d]
                if not estao_ok(p1, p2, matriz):
                    return 'N'
    return 'Y'


def main():
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            m, n, p = map(int, line.split())
            matriz = preenche_matriz(p)
            print(solve_this_problem(matriz))


main()
