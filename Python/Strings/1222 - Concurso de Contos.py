"""
Autor: Pierre Vieira
Data da submissão: 28/01/2020 00:04:15
"""
from math import ceil


def solve_this_problem(conto):
    """Retorna o número mínimo de páginas que o conto ocupa"""
    qtde_linhas = 1
    palavras = conto.split()
    words = iter(palavras)
    palavra = next(words)
    while True:
        linha = ''
        while len(linha) + len(palavra) <= maximo_caracteres_por_linha:
            linha += palavra+' '
            if len(linha) > maximo_caracteres_por_linha:
                linha = linha[:len(linha)-1:]
            try:
                palavra = next(words)
            except StopIteration:
                return ceil(qtde_linhas / maximo_linhas_por_pagina)
        else:  # Sim, tem else pra while em python
            qtde_linhas += 1


while True:
    try:
        numero_de_palavras_do_conto, maximo_linhas_por_pagina, maximo_caracteres_por_linha = map(int, input().split())
    except EOFError:
        break
    else:
        print(solve_this_problem(input()))
