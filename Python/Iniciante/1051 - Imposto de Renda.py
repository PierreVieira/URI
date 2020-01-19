"""
Autor: Pierre Vieira
Data da submissão: 26/01/2019 23:00:32
"""
salario = float(input())
imposto = 0
if salario <= 2000:
    print("Isento")
else:
    if 2000.01 <= salario <= 3000:
        x = salario - 2000
        imposto = x *0.08
    elif 3000.01 <= salario <= 4500:
        x = salario - 2000
        imposto = 1000*0.08
        x -= 1000
        imposto += x*0.18
    else:
        x = salario - 2000
        imposto = 1000*0.08
        x -= 1000
        imposto += 1500*0.18
        x -= 1500
        imposto += x*0.28
    print("R$ {:.2f}".format(imposto))
