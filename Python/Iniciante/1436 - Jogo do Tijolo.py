"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 21:38:03
"""
from statistics import median
for c in range(int(input())):
    print('Case {}: {}'.format(c + 1, median(input().split()[1:])))
