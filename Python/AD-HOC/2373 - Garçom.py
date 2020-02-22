"""
Autor: Pierre Vieira
Data da submissão: 22/02/2020 00:08:40
"""
s = 0
for c in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        s += b
print(s)
