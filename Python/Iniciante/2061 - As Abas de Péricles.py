"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 20:06:07
"""
a, b = map(int, input().split())
for c in range(b):
    if input() == 'clicou':
        a -= 1
    else:
        a += 1
print(a)
