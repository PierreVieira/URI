"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 12:33:46
"""
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    volume = a*b*c
    print(int(volume**(1/3)))
