"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 15:53:23
"""
qtde_pecas = int(input())
numeros = tuple(sorted(map(int, input().split())))
if numeros[0] != 1:
    print(1)
elif numeros[-1] != qtde_pecas:
    print(qtde_pecas)
else:
    for c in range(1, len(numeros)):
        if numeros[c] - numeros[c - 1] != 1:
            print(numeros[c] - 1)
            break
