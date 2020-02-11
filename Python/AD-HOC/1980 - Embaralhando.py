"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 01:09:09
"""
from math import factorial

while True:
    linha = input().strip()
    if linha == '0':
        break
    palavras = linha.split()
    for palavra in palavras:
        print(factorial(len(palavra)))

