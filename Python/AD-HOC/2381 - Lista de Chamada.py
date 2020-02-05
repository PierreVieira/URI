"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 09:28:02
"""
n, k = map(int, input().split())
lista = [input() for c in range(n)]
lista.sort()
print(lista[k - 1])
