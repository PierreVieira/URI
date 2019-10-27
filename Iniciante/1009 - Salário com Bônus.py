"""
Autor: Pierre Vieira
Data da submissão: 16/01/2019 23:58:26
"""
nome = input()
salario = float(input())
total_vendas = float(input())
comissao = float(total_vendas*0.15)
print("TOTAL = R$ {:.2f}".format(salario+comissao))
