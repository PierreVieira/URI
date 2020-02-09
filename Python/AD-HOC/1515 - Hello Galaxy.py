"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 12:52:37
"""
while True:
    n = int(input())
    if n == 0:
        break
    nome_planetas = []
    tempo_planetas = []
    for c in range(n):
        nome_planeta, ano, tempo = input().split()
        ano_lancamento = int(ano) - int(tempo)
        nome_planetas.append(nome_planeta)
        tempo_planetas.append(ano_lancamento)
    print(nome_planetas[tempo_planetas.index(min(tempo_planetas))])
