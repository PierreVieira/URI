"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 18:05:03
"""


def formar_triangulo_pascal():
    triangulo_de_pascal = [[1], [1, 1]]
    for c in range(1, n - 1):
        linha_pascal = [1]
        for d in range(1, c + 1):
            linha_pascal.append(triangulo_de_pascal[-1][d - 1] + triangulo_de_pascal[-1][d])
        linha_pascal.append(1)
        triangulo_de_pascal.append(linha_pascal.copy())
    return triangulo_de_pascal


for c in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    else:
        triangulo_de_pascal = formar_triangulo_pascal()
        print(sum(tuple(map(sum, triangulo_de_pascal))))
