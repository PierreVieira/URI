"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 00:56:58
"""
for c in range(int(input())):
    n = int(input())
    notas = tuple(map(int, input().split()))
    maior_nota = max(notas)
    lista_sequencia = []
    qtde_aparicoes_maior_nota = 0
    for nota in notas:
        if nota != maior_nota:
            lista_sequencia.append(qtde_aparicoes_maior_nota)
            qtde_aparicoes_maior_nota = 0
        else:
            qtde_aparicoes_maior_nota += 1
    maior_seq = max((max(lista_sequencia), qtde_aparicoes_maior_nota))
    print('Caso #{}: {}'.format(c + 1, maior_seq))