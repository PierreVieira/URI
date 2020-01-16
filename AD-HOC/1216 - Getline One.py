"""
Autor: Pierre Vieira
Data da submissão: 15/01/2020 19:21:02
"""
from statistics import mean

lista = []
while True:
    try:
        linha1, linha2 = input(), int(input())
    except EOFError:
        print('{:.1f}'.format(mean(lista)))
        break
    else:
        lista.append(linha2)
