"""
Autor: Pierre Vieira
Data da submissão: 01/02/2020 17:10:26
"""
n = int(input())
la, lb = map(int, input().split())
sa, sb = map(int, input().split())
if la <= n <= lb and sa <= n <= sb:
    print('possivel')
else:
    print('impossivel')