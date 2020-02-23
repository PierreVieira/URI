"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 17:07:39
"""
q, e = map(int, input().split())
identificacao_escritorios = list(map(int, input().split()))
for c in range(q):
    n = int(input())
    if n in identificacao_escritorios:
        print(0)
    else:
        print(1)
    identificacao_escritorios.append(n)
