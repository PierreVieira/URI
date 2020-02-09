"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 13:52:08
"""
lista_traducoes = [(input(), input()) for c in range(int(input()))]
lista_nomes = [(input(), input()) for c in range(int(input()))]
for pessoa in lista_nomes:
    for lingua in lista_traducoes:
        if pessoa[1] == lingua[0]:
            feliz_natal = lingua[1]
            break
    print(pessoa[0])
    print(feliz_natal)
    print()
