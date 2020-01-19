"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 18:54:35
"""
n = int(input())
for c in range(n):
    pontuacao_maria = 0
    pontuacao_joao = 0
    for d in range(3):
        a, b = map(int, input().split())
        pontuacao_joao += a * b
    for d in range(3):
        a, b = map(int, input().split())
        pontuacao_maria += a * b
    if pontuacao_maria > pontuacao_joao:
        print('MARIA')
    else:
        print('JOAO')
