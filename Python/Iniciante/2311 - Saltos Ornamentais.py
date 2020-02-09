"""
Autor: Pierre Vieira
Data da submissão: 08/02/2020 23:45:42
"""
for c in range(int(input())):
    nome = input()
    peso = float(input())
    notas = list(sorted(map(float, input().split())))
    soma = sum(notas[1:len(notas)-1])
    print('{} {:.2f}'.format(nome, soma*peso))
