"""
Autor: Pierre Vieira
Data da submissão: 27/01/2019 01:32:11
"""
casos_teste = int(input())
while casos_teste != 0:
    string = input()
    texto = list(string)
    if not(1 <= len(string) <= 1000):
        break
    for c in range(0, len(string)):
        if texto[c].isalpha():
            texto[c] = chr(ord(texto[c]) + 3)
    ultimo_caractere = len(string) -1
    for c in range(0, len(string)//2):
        aux = texto[c]
        texto[c] = texto[ultimo_caractere]
        texto[ultimo_caractere] = aux
        ultimo_caractere -= 1
    for c in range(len(string)//2, len(string)):
        texto[c] = chr(ord(texto[c]) - 1)
    print(''.join(texto))
    casos_teste -= 1