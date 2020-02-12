"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 01:12:00
"""


def preenche_jogadores():
    for c in range(qtde_jogadores):
        nome_jogador, nivel_habilidade = input().split()
        jogadores.append((int(nivel_habilidade), nome_jogador))


def preenche_times():
    c = 0
    for jogador in jogadores:
        times[c].append(jogador)
        c += 1
        if c == qtde_times:
            c = 0


def infos():
    cont = 0
    for time in times:
        cont += 1
        print('Time {}'.format(cont))
        lista_nomes = [jogador[1] for jogador in time]
        for nome_jogador in sorted(lista_nomes):
            print(nome_jogador)
        print()


qtde_jogadores, qtde_times = map(int, input().split())
jogadores = []
preenche_jogadores()
jogadores.sort(reverse=True)
times = [[] for d in range(qtde_times)]
preenche_times()
infos()
