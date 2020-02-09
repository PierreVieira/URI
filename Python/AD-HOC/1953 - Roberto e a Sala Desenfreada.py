"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 12:40:28
"""


def solve_this_problem():
    epr = ehd = intrusos = 0
    for aluno in lista_alunos:
        if aluno[1] == 'EPR':
            epr += 1
        elif aluno[1] == 'EHD':
            ehd += 1
        else:
            intrusos += 1
    print('EPR: {}\nEHD: {}\nINTRUSOS: {}'.format(epr, ehd, intrusos))


while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        lista_alunos = [input().split() for c in range(n)]
        solve_this_problem()