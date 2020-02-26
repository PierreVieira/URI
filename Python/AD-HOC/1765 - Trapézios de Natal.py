"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 16:13:10
"""
while True:
    n = int(input())
    if n == 0:
        break
    for c in range(n):
        q, a, b = map(float, input().split())
        print('Size #{}:\nIce Cream Used: {:.2f} cm2'.format(c + 1, q * (5 * (a + b) / 2)))
    print()