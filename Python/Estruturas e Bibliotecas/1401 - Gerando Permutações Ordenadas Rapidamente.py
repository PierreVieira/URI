"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 16:40:21
"""
from itertools import permutations

for c in range(int(input())):
    for palavra in sorted(set(permutations(input()))):
        print(''.join(palavra))
    print()
