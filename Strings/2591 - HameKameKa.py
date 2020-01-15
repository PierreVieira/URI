"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 22:04:53
"""
n = int(input())
for c in range(n):
    entrada = input().split('me')
    print('k', end='a'*entrada[0].count('a')*entrada[1].count('a')+'\n')
