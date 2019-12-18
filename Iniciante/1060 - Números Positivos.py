"""
Autor: Pierre Vieira
Data da submissão: 27/01/2019 18:26:55
"""
positivos = 0
for c in range(0, 6):
    valor = float(input())
    if valor > 0:
        positivos += 1
print("{} valores positivos".format(positivos))
