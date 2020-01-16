"""
Autor: Pierre Vieira
Data da submissão: 16/01/2020 14:29:31
"""


def nao_tem_repeditos(n):
    for caracter in n:
        if n.count(caracter) > 1:
            return False
    return True


def solve_this_problem(n, m):
    cont = 0
    while n <= m:
        if nao_tem_repeditos(str(n)):
            cont += 1
        n += 1
    return cont


def main():
    while True:
        try:
            n, m = map(int, input().split())
        except EOFError:
            break
        else:
            print(solve_this_problem(n, m))


main()
