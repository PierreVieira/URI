"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 16:01:20
"""
n, m = map(int, input().split())
cont = 0
for c in range(n):
    if not 0 in map(int, input().split()):
        cont += 1
print(cont)
