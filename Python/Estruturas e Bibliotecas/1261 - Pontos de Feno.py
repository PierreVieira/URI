"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 01:28:13
"""
a, b = map(int, input().split())
dicionario = {}
for c in range(a):
    chave, value = input().split()
    dicionario[chave] = float(value)
for c in range(b):
    soma = 0
    while True:
        linha = input()
        if linha == '.':
            break
        for palavra in linha.split():
            try:
                soma += dicionario[palavra]
            except KeyError:
                pass
    print(int(soma))
