"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 13:33:58
"""
n = int(input())
linha = tuple(map(int, input().split()))
if linha.count(0) > n/2:
    print('Y')
else:
    print('N')