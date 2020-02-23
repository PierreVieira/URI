"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 16:13:19
"""
tupla_pontuacoes = tuple(map(float, input().split()))
minimo = min(tupla_pontuacoes)
if tupla_pontuacoes.count(minimo) > 1:
    print('Empate')
else:
    print(('Otavio', 'Bruno', 'Ian')[tupla_pontuacoes.index(minimo)])
