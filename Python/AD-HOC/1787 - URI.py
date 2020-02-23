"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 12:29:07
"""
from math import log2


def potencia_de_2(pontuacao):
    y = log2(pontuacao)
    booleano = y.is_integer() and pontuacao != 1
    return booleano


def atualizar_pontuacoes():
    if potencia_de_2(uilton):
        pontuacoes['uilton'] += 1
        if uilton > rita and uilton > ingred:
            pontuacoes['uilton'] += 1
    if potencia_de_2(rita):
        pontuacoes['rita'] += 1
        if rita > uilton and rita > ingred:
            pontuacoes['rita'] += 1
    if potencia_de_2(ingred):
        pontuacoes['ingred'] += 1
        if ingred > uilton and ingred > rita:
            pontuacoes['ingred'] += 1


def vencedor():
    if pontuacoes['uilton'] > pontuacoes['rita'] and pontuacoes['uilton'] > pontuacoes['ingred']:
        print('Uilton')
    elif pontuacoes['rita'] > pontuacoes['uilton'] and pontuacoes['rita'] > pontuacoes['ingred']:
        print('Rita')
    elif pontuacoes['ingred'] > pontuacoes['rita'] and pontuacoes['ingred'] > pontuacoes['uilton']:
        print('Ingred')
    else:
        print('URI')


while True:
    pontuacoes = {'uilton': 0, 'rita': 0, 'ingred': 0}
    n = int(input())
    if n == 0:
        break
    for c in range(n):
        uilton, rita, ingred = map(int, input().split())
        atualizar_pontuacoes()
    vencedor()
