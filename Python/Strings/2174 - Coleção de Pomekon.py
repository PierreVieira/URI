"""
Autor: Pierre Vieira
Data da submissão: 27/01/2020 23:04:55
"""
conjunto = set()
for c in range(int(input())):
    conjunto.add(input())
print('Falta(m) {} pomekon(s).'.format(151 - len(conjunto)))
