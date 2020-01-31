"""
Autor: Pierre Vieira
Data da submissão: 31/01/2020 17:06:16
"""


def qtde_trocas_possiveis():
    nao_repetidas_alice = set(cartas_alice)
    nao_repetidas_beatriz = set(cartas_beatriz)
    cartas_que_alice_tem_e_beatriz_nao_tem = tuple(x for x in nao_repetidas_alice if not x in nao_repetidas_beatriz)
    cartas_que_beatriz_tem_e_alice_nao_tem = tuple(x for x in nao_repetidas_beatriz if not x in nao_repetidas_alice)
    qtde_a, qtde_b = len(cartas_que_alice_tem_e_beatriz_nao_tem), len(cartas_que_beatriz_tem_e_alice_nao_tem)
    return min(qtde_a, qtde_b)


while True:
    qtde_cartas_alice, qtde_cartas_beatriz = map(int, input().split())
    if qtde_cartas_alice == qtde_cartas_beatriz == 0:
        break
    cartas_alice = list(sorted(map(int, input().split())))
    cartas_beatriz = list(sorted(map(int, input().split())))
    print(qtde_trocas_possiveis())
