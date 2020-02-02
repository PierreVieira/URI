"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 17:17:34
"""
for c in range(int(input())):
    lista_instrucoes = []
    for d in range(int(input())):
        instrucao = input()
        if instrucao == 'LEFT':
            lista_instrucoes.append(-1)
        elif instrucao == 'RIGHT':
            lista_instrucoes.append(1)
        else:
            lista_instrucoes.append(lista_instrucoes[int(instrucao.split()[-1]) - 1])
    print(sum(lista_instrucoes))
