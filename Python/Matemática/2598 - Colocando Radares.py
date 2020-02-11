"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 18:12:02
"""
from math import ceil

for c in range(int(input())):
    n, m = map(int, input().split())
    print(ceil(n/m))
