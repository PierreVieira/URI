"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 01:44:26
"""
queda = 0
n = int(input())
lista = list(map(int, input().split()))
for c in range(1, len(lista)):
    if lista[c] < lista[c - 1]:
        queda = c + 1
        break
print(queda)
