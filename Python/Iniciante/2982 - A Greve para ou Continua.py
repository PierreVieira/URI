"""
Autor: Pierre Vieira
Data da submissão: 10/01/2020 15:34:06
"""
n = int(input())
lista_gastos = []
lista_ganhos = []
for c in range(n):
    linha = input().split()
    ganho_gasto, valor = linha[0], int(linha[1])
    if ganho_gasto == 'G':
        lista_gastos.append(valor)
    else:
        lista_ganhos.append(valor)
if sum(lista_ganhos) >= sum(lista_gastos):
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
