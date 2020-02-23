"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 16:58:47
"""


def solve_this_problem():
    dicionario_pos = {}
    for c in range(n):
        dicionario_pos.update({linha[c]: c})
    linha2 = list(map(int, input().split()))
    cont = 0
    for i in range(len(linha2)):
        for j in range(i + 1, len(linha2)):
            if dicionario_pos[linha2[j]] < dicionario_pos[linha2[i]]:
                linha2[i], linha2[j] = linha2[j], linha2[i]
                cont += 1
    print(cont)


while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        linha = tuple(map(int, input().split()))
        solve_this_problem()
