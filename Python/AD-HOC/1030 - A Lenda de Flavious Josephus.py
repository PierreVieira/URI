"""
Autor: Pierre Vieira
Data da submissão: 02/03/2019 11:56:10
"""


def solucao(n, k):
    x = 0
    for c in range(2, n + 1):
        x = (x + k) % c
    return x


nc = int(input())
c = 0
while nc > 0:
    nc -= 1
    c += 1
    linha = input().split()
    n, k = map(int, linha)
    print("Case {}: {}".format(c, solucao(n, k) + 1))
