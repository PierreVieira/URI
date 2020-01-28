"""
Autor: Pierre Vieira
Data da submissão: 28/01/2020 00:38:34
"""
while True:
    n = int(input())
    if n == 0:
        break
    lista = list(map(int, input().split()))
    maximo = max(lista)
    minimo = min(lista)
    lista2 = list(map(lambda x: minimo-1 if x == maximo else x, lista))
    print(lista2.index(max(lista2))+1)
