"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 17:21:15
"""

rafael = lambda x, y: (3 * x) ** 2 + y ** 2
beto = lambda x, y: 2 * x ** 2 + (5 * y) ** 2
carlos = lambda x, y: -100 * x + y ** 3
for c in range(int(input())):
    x, y = map(int, input().split())
    valores = (rafael(x, y), beto(x, y), carlos(x, y))
    nomes = ('Rafael', 'Beto', 'Carlos')
    print(nomes[valores.index(max(valores))]+' ganhou')
