"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 11:17:17
"""
for c in range(int(input())):
    qt, s = map(int, input().split())
    vetor = tuple(map(int, input().split()))
    try:
        print(vetor.index(s) + 1)
    except ValueError:
        diferencas = tuple(map(lambda x: abs(s - x), vetor))
        print(diferencas.index(min(diferencas)) + 1)
