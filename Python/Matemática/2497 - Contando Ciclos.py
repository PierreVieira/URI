"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 13:11:52
"""
cont = 0
while True:
    cont += 1
    n = int(input())
    if n == -1:
        break
    print('Experiment {}: {} full cycle(s)'.format(cont, n // 2))
