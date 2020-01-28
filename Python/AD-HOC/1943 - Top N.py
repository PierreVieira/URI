"""
Autor: Pierre Vieira
Data da submissão: 28/01/2020 00:45:42
"""
tupla_colocacoes = (1, 3, 5, 10, 25, 50, 100)
n = int(input())
print('Top', end=' ')
if n in tupla_colocacoes:
    print(n)
else:
    for c in tupla_colocacoes:
        if n < c:
            print(c)
            break
