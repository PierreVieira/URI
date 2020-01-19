"""
Autor: Pierre Vieira
Data da submissão: 25/01/2019 01:09:01
"""
linha = input().split(" ")
X, Y = linha
x = float(X)
y = float(Y)
if x == 0 and y == 0:
    print("Origem")
elif x == 0 and y !=0:
    print("Eixo Y")
elif x != 0 and y == 0:
    print("Eixo X")
elif x > 0 and y >0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x <0 and y < 0:
    print("Q3")
else:
    print("Q2")
