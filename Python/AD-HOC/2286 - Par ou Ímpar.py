"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 12:01:14
"""


def solve_this_problem():
    nome_par, nome_impar = input(), input()
    for c in range(n):
        n1, n2 = map(int, input().split())
        if (n1 + n2) % 2 == 0:
            print(nome_par)
        else:
            print(nome_impar)


cont = 1
while True:
    n = int(input())
    if n == 0:
        break
    print('Teste {}'.format(cont))
    solve_this_problem()
    print()
    cont += 1
