"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 09:41:49
"""
n = int(input())


def formar_palavra():
    s = ''
    ultimo_i = -1
    for c in palavra:
        for i in range(ultimo_i + 1, len(linha)):
            if linha[i] == c:
                s += linha[i]
                ultimo_i = i
                break
    return s


def contem():
    formada = formar_palavra()
    if formada == palavra:
        return True
    return False


for c in range(n):
    linha = input()
    for q in range(int(input())):
        palavra = input()
        if contem():
            print('Yes')
        else:
            print('No')
