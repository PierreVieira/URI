"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 16:49:03
"""
n, t0, l = map(int, input().split())
a = b = 0
cont = 0
for carta in tuple(int(input()) for c in range(n - 1)):
    limite = abs(carta - t0)
    if limite <= l:
        t0 = carta
        if cont % 2 == 0:
            a += limite
        else:
            b += limite
    cont += 1
print(a, b)
