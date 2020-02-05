"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 09:53:39
"""


def remover_char_especial(palavra):
    """Remove tudo que não é letra"""
    s = ''
    for char in palavra:
        if char.isalpha():
            s += char
    return s


def tempos(palavras):
    lista_tempos = []
    cont = 0
    for palavra in palavras:
        cont += len(palavra)
        if palavra.lower() == 'perdi' or palavra.lower() == 'jogo':
            lista_tempos.append(cont)
            cont = 0
    return lista_tempos


for c in range(int(input())):
    palavras = tuple(map(remover_char_especial, input().split()))
    print(max(tempos(palavras)))
