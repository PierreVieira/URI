"""
Autor: Pierre Vieira
Data da submissão: 25/01/2019 01:50:33
"""
linha = input().split(" ")
x, y, z = linha
a = float(x)
b = float(y)
c = float(z)
cont = 0
aux = 0
while cont == 0:
    cont = 1
    if a < b:
        aux = a
        a = b
        b = aux
        cont = 0
    if a < c:
        aux = a
        a = c
        c = aux
        cont = 0
    if b < c:
        aux = b
        b = c
        c = aux
        cont = 0
if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if a==b and b != c or a==c and b != c or b==c and a!=c:
        print("TRIANGULO ISOSCELES")
