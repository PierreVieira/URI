"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 16:47:49
"""
qtde_linhas, qtde_colunas = map(int, input().split())
matriz_qtde_minhocas = [tuple(map(int, input().split())) for c in range(qtde_linhas)]
lista_soma_qtde_minhocas = list(map(lambda lista: sum(lista), matriz_qtde_minhocas))
for d in range(qtde_colunas):
    lista_coluna = []
    for e in range(qtde_linhas):
        lista_coluna.append(matriz_qtde_minhocas[e][d])
    lista_soma_qtde_minhocas.append(sum(lista_coluna))
print(max(lista_soma_qtde_minhocas))
