"""
Autor: Pierre Vieira
Data da submissão: 	18/02/2020 08:11:31
"""
c, p, f = map(int, input().split())
if p//c >= f:
    print('S')
else:
    print('N')
