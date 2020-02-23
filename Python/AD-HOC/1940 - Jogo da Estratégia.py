"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 15:14:53
"""
qtde_jogadores, qtde_jogadas = map(int, input().split())
jogadas = tuple(map(int, input().split()))
jogadas_separadas = [[] for c in range(qtde_jogadores)]
for i in range(len(jogadas)):
    jogadas_separadas[i % qtde_jogadores].append(jogadas[i])
pontuacoes = tuple(map(lambda lista: sum(lista), jogadas_separadas))
pontuacao_maxima = max(pontuacoes)


def vencedor():
    for d in range(len(pontuacoes)-1, -1, -1):
        if pontuacoes[d] == pontuacao_maxima:
            print(d + 1)
            break


vencedor()
