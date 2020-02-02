"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 17:10:45
"""
for c in range(int(input())):
    partida1, partida2 = tuple(map(int, input().split(' x '))), tuple(map(int, input().split(' x ')))
    qtde_gols_time_1_primeira_partida, qtde_gols_time_2_primeira_partida, qtde_gols_time_1_segunda_partida, qtde_gols_time_2_segunda_partida = partida1[0], partida1[1], partida2[1], partida2[0]
    if qtde_gols_time_1_primeira_partida + qtde_gols_time_1_segunda_partida > qtde_gols_time_2_primeira_partida + qtde_gols_time_2_segunda_partida:
        print('Time 1')
    elif qtde_gols_time_1_primeira_partida + qtde_gols_time_1_segunda_partida < qtde_gols_time_2_primeira_partida + qtde_gols_time_2_segunda_partida:
        print('Time 2')
    elif qtde_gols_time_1_segunda_partida > qtde_gols_time_2_primeira_partida:
        print('Time 1')
    elif qtde_gols_time_2_primeira_partida > qtde_gols_time_1_segunda_partida:
        print('Time 2')
    else:
        print('Penaltis')

