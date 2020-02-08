"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 19:45:57
"""
n = int(input())
for c in range(n):
    tupla_nomes = tuple(input().split())
    nome1, escolha1, nome2, escolha2 = tupla_nomes
    soma = sum(map(int, input().split()))
    if soma % 2 == 0 and escolha1 == 'PAR':
        print(nome1)
    elif soma % 2 == 0 and escolha1 == 'IMPAR':
        print(nome2)
    elif soma % 2 == 1 and escolha1 == 'IMPAR':
        print(nome1)
    else:
        print(nome2)
