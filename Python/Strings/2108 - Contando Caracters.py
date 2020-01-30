"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 17:35:42
"""


def encontra_maior_palavra(lista_palavras, maior_palavra):
    for palavra in lista_palavras:
        if len(palavra) >= len(maior_palavra):
            maior_palavra = palavra
    return maior_palavra


cont = 0
while True:
    linha = input()
    if linha == '0':
        break
    lista_palavras = linha.split()
    if cont == 0:
        biggest_word = encontra_maior_palavra(lista_palavras, lista_palavras[0])
    else:
        biggest_word = encontra_maior_palavra(lista_palavras, biggest_word)
    cont += 1
    lista_qtde_char = [str(len(palavra)) for palavra in lista_palavras]
    print('-'.join(lista_qtde_char))
print('\nThe biggest word: {}'.format(biggest_word))