"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 17:24:16
"""
for c in range(int(input())):
    n = int(input())
    print(str(sorted(map(int, input().split()))).replace('[', '').replace(']', '').replace(',', ''))
