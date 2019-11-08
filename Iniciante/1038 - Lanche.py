"""
Autor: Pierre Vieira
Data da submissão: 23/01/2019 00:39:28
"""
linha = input().split(" ")
a, b = linha
codigo = int(a)
qtde_valor = int(b)
if codigo == 1:
    valor = 4
elif codigo == 2:
    valor = 4.5
elif codigo == 3:
    valor = 5
elif codigo == 4:
    valor = 2
else:
    valor = 1.5
print("Total: R$ {:.2f}".format(valor*qtde_valor))
