"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 02:40:50
"""
for c in range(int(input())):
    lista_compras = list(sorted(set(input().split())))
    for d in range(len(lista_compras) - 1):
        print(lista_compras[d], end=' ')
    print(lista_compras[len(lista_compras) - 1])
