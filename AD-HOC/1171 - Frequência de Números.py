"""
Autor: Pierre Vieira
Data da submissão: 02/01/2020 23:38:08
"""

n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
lista.sort()
ja_foi = []
for numero in lista:
    if not(numero in ja_foi):
        print('{} aparece {} vez(es)'.format(numero, lista.count(numero)))
        ja_foi.append(numero)
