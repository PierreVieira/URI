"""
Autor: Pierre Vieira
Data da submissão: 03/03/2019 15:13:50
"""
while True:
    linha = input().split()
    l, c, r1, r2 = map(int, linha)
    if l == c == r1 == r2 == 0:
        break
    if min(l, c) < max(r1, r2)*2:
        print('N')
    else:
        r1 += r2
        l -= r1
        c -= r1
        if r1**2 > (l**2 + c**2):
            print('N')
        else:
            print('S')
