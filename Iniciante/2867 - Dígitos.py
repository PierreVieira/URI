"""
Autor: Pierre Vieira
Data da submissão: 17/01/2020 21:10:16
"""

n = int(input())
for c in range(n):
    a, b = map(int, input().split())
    print(len(str(a**b)))
