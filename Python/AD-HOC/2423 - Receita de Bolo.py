"""
Autor: Pierre Vieira
Data da submissão: 10/02/2020 21:24:05
"""
a, b, c = map(int, input().split())
qtde_bolos = min(a//2, b//3, c//5)
print(qtde_bolos)
