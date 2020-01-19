"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 21:34:58
"""

n = int(input())
hobits = humanos = elfos = anoes = magos = 0
for c in range(n):
    pessoa = tuple(map(str, input().split()))[1]
    if pessoa == 'A':
        anoes += 1
    elif pessoa == 'E':
        elfos += 1
    elif pessoa == 'H':
        humanos += 1
    elif pessoa == 'M':
        magos += 1
    else:
        hobits += 1
print('{} Hobbit(s)\n{} Humano(s)\n{} Elfo(s)\n{} Anao(s)\n{} Mago(s)'.format(hobits, humanos, elfos, anoes, magos))