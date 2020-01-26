"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 16:59:30
"""
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    bilhetes = list(map(int, input().split()))
    conjunto = set()
    for n in bilhetes:
        if bilhetes.count(n) > 1:
            conjunto.add(n)
    print(len(conjunto))