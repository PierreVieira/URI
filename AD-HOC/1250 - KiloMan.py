"""
Autor: Pierre Vieira
Data da submissão: 16/01/2020 14:22:27
"""


def solve_this_problem(s_alturas, s_pulos):
    qtde_vezes_atingido = 0
    pulo_altura = zip(s_alturas, s_pulos)
    tomou_tiro_parado = lambda x: (x[0] == 1 or x[0] == 2) and x[1] == 'S'
    tomou_tiro_pulando = lambda x: x[0] > 2 and x[1] == 'J'
    for c in pulo_altura:
        if tomou_tiro_parado(c) or tomou_tiro_pulando(c):
            qtde_vezes_atingido += 1
    return qtde_vezes_atingido


def main():
    n = int(input())
    for c in range(n):
        numero_tiros = int(input())
        sequencia_alturas = list(map(int, input().split()))
        sequencia_pulos = input()
        print(solve_this_problem(sequencia_alturas, list(sequencia_pulos)))


main()
