"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 10:41:23
"""


def conserta_palavra(palavra):
    if len(palavra) != 3:
        return palavra
    elif palavra[0:2] == 'OB':
        return 'OBI'
    elif palavra[0:2] == 'UR':
        return 'URI'
    return palavra


n = int(input())
palavras = input().split()
palavras = tuple(map(conserta_palavra, palavras))
for c in range(len(palavras)-1):
    print(palavras[c], end=' ')
print(palavras[len(palavras) - 1])
