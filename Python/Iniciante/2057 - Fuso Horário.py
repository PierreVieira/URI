"""
Autor: Pierre Vieira
Data da submissão: 31/01/2020 00:08:15
"""
a, b, c = map(int, input().split())
soma = a + b + c
if 0 <= soma <= 23:
    print(soma)
elif soma >= 24:
    print(soma - 24)
else:
    print(24 + soma)
