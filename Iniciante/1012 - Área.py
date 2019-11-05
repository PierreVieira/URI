"""
Autor: Pierre Vieira
Data da submissão: 19/01/2019 14:58:55
"""
linha1 = input().split(" ")
a,b,c = linha1
triangulo = float(float(a)*float(c))/2
circulo = float(3.14159*float(c)*float(c))
trapezio = float(float(float(a)+float(b))*float(c))/2
quadrado = float(b)**2
retangulo = float(float(a)*float(b))
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(triangulo, circulo, trapezio, quadrado, retangulo))
