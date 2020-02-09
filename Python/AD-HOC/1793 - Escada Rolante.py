"""
Autor: Pierre Vieira
Data da submissão: 08/02/2020 20:38:58
"""


def solve_this_problem():
    tempo_total = 0
    if len(tempos) == 1:
        return 10
    for c in range(len(tempos)-1):
        dif = tempos[c+1] - tempos[c]
        if dif > 10:
            tempo_total += 10
        else:
            tempo_total += dif
    return tempo_total + 10


while True:
    if int(input()) == 0:
        break
    tempos = tuple(map(int, input().split()))
    print(solve_this_problem())
