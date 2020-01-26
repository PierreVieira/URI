"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 15:31:23
"""
while True:
    l, r = map(int, input().split())
    if l == r == 0:
        break
    print(l + r)
