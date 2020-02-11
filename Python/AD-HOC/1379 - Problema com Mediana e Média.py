"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 16:18:57
"""
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(2*a - b)
