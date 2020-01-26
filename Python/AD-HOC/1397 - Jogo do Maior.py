"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 15:51:11
"""
while True:
    n = int(input())
    if n == 0:
        break
    lista = [tuple(map(int, input().split())) for c in range(n)]
    cont1 = cont2 = 0
    for e in lista:
        if e[0] > e[1]:
            cont1 += 1
        elif e[0] < e[1]:
            cont2 += 1
    print(cont1, cont2)
