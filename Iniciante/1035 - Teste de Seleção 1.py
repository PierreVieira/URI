"""
Autor: Pierre Vieira
Data da submissão: 04/05/2018 16:40:21
"""
linha = input().split(" ")
a, b, c, d = linha
A = int(a)
B = int(b)
C = int(c)
D = int(d)
if B > C and D > A and C+D > A+B and C > 0 and D > 0 and A%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
