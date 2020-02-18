"""
Autor: Pierre Vieira
Data da submissão: 18/02/2020 10:08:07
"""


def formatar(n):
    while len(n) > 1:
        n = sum(map(lambda x: int(x), n))
        n = str(n)
    return int(n)


while True:
    n1, n2 = input().split()
    if n1 == n2 == '0':
        break
    s1, s2 = formatar(n1), formatar(n2)
    if s1 > s2:
        print(1)
    elif s1 < s2:
        print(2)
    else:
        print(0)