"""
Autor: Pierre Vieira
Data da submissão: 28/01/2020 00:23:00
"""
lista_qtde_pinos = list(map(int, input().split()))
maior_qtde_pinos = max(lista_qtde_pinos)
lista_qtde_pinos.remove(maior_qtde_pinos)
maior_qtde_pinos -= len(lista_qtde_pinos)
print(sum(lista_qtde_pinos)+maior_qtde_pinos)
