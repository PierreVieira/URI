"""
Autor: Pierre Vieira
Data da submissão: 17/01/2019 01:13:31
"""
linha = input().split(" ")
A, B, C = linha
a = float(A)
b = float(B)
c = float(C)
if not(a >= b+c or b >= a+c or c >= a+b):
    perimetro = a + b + c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    trapezio = (a+b)*c/2
    print("Area = {:.1f}".format(trapezio))
