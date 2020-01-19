"""
Autor: Pierre Vieira
Data da submissão: 22/01/2019 23:55:21
"""
n_dias = int(input())
ano = n_dias//365
mes = (n_dias%365)//30
dias = (n_dias%365)%30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, dias))
