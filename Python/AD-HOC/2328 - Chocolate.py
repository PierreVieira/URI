"""
Autor: Pierre Vieira
Data da submissão: 16/02/2020 17:20:31
"""
n = int(input())
divisoes = tuple(map(int, input().split()))
print(sum(map(lambda x: x - 1, divisoes)))
