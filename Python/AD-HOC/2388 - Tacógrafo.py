"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 00:40:21
"""
lista = [tuple(map(int, input().split())) for c in range(int(input()))]
distancia = 0
for tupla in lista:
    distancia += tupla[0]*tupla[1]
print(distancia)
