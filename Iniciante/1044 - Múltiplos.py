"""
Autor: Pierre Vieira
Data da submissão: 25/01/2019 01:31:06
"""
linha = input().split(" ")
A, B = linha
a = int(A)
b = int(B)
if a%b == 0 and a > b or b%a == 0 and b > a:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
