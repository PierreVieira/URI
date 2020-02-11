"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 00:52:04
"""
for c in range(int(input())):
    n, k = map(int, input().split())
    print(n % k + n // k)
