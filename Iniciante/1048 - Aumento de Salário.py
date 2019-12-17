"""
Autor: Pierre Vieira
Data da submissão: 25/01/2019 21:16:06
"""
salario = float(input())
if 0 <= salario <= 400: #15%
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(salario*1.15, salario*0.15))
elif salario <= 800: #12%
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(salario*1.12, salario*0.12))
elif salario <= 1200: #10%
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(salario*1.1, salario*0.1))
elif salario <= 2000: #7%
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(salario*1.07, salario*0.07))
else: #4%
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(salario*1.04, salario*0.04))
