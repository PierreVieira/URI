"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 16:36:21
"""
while True:
    linha = input()
    n1 = int(linha[:linha.find('+')][::-1])
    n2 = int(linha[linha.find('+')+1:linha.find('=')][::-1])
    n3 = int(linha[linha.find('=')+1:][::-1])
    print(n1 + n2 == n3)
    if linha == '0+0=0':
        break
