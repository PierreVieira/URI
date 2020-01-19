"""
Autor: Pierre Vieira
Data da submissão: 22/02/2019 14:17:02
"""
def mdc(n1, n2):
    while n2%n1 != 0:
        aux = n2
        n2 = n1
        n1 = aux%n1
    return n1

n = int(input())
while n > 0:
    n-=1
    linha = input().split()
    x, y = list(map(int, linha))
    if x > y:
        aux = x
        x = y
        y = aux
    print(mdc(x, y))