"""
Autor: Pierre Vieira
Data da submissão: 16/01/2020 17:03:39
"""


def solve_this_problem():
    palavras = []
    for seq in entrada:
        if seq[1] == 'chirrin' and entrada.count([seq[0], 'chirrin']) > entrada.count([seq[0], 'chirrion']):
            palavras.append(seq[0])
    palavras.sort()
    for palavra in palavras:
        print(palavra)


n = int(input())
for c in range(n):
    v = int(input())
    print('TOTAL')
    entrada = []
    for d in range(v):
        entrada.append(input().split())
    solve_this_problem()
