"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 17:24:02
"""
linhas, colunas = map(int, input().split())
matriz = []
for c in range(linhas):
    matriz.extend(input().split())
lista_v = [elemento for elemento in matriz if elemento[1] == 'V']
lista_v.sort(reverse=True)
lista_d = [elemento for elemento in matriz if elemento[1] == 'D']
lista_d.sort(reverse=True)
for v in lista_v:
    print(v)
for d in lista_d:
    print(d)
