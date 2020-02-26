"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 13:06:32
"""
n = int(input())
matriz = [list(map(int, input().split())) for c in range(n)]
coletadas = []
for x in range(2*n):
    c, d = map(int, input().split())
    coletadas.append(matriz[c - 1][d - 1])
print(len(set(coletadas)))
