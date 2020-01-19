"""
Autor: Pierre Vieira
Data da submissão: 18/01/2020 21:23:25
"""
valor_caixa, gasto_diario = map(int, input().split())
more_days = int(valor_caixa/gasto_diario)
dia_fechamento = 21+more_days
if dia_fechamento > 30:
    print('A UFSC fecha dia {} de outubro.'.format(dia_fechamento - 30))
else:
    print('A UFSC fecha dia {} de setembro.'.format(dia_fechamento))
