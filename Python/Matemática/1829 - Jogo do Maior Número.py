"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 01:45:28
Referência: https://www.life2coding.com/uri-online-judge-solution-1829-biggest-number-game-intermediate-problem/
"""
from math import log, pi, e


def saida():
    if pedro_vencidas > lucas_vencidas:
        print('Campeao: Pedro!')
    elif pedro_vencidas < lucas_vencidas:
        print('Campeao: Lucas!')
    else:
        print('A competicao terminou empatada!')
    for resultado_rodada in lista_resultado:
        print(resultado_rodada)


def my_factorial(n):
    resultado = 1
    for i in range(1, n):
        resultado *= i
    return resultado


def calcular_entradas():
    cont_rodada = 0
    global lucas_vencidas, pedro_vencidas
    for c in range(int(input())):
        cont_rodada += 1
        rodada = (input(), input())
        lucas_n1, lucas_n2 = map(int, rodada[0].split('^'))
        n_pedro = int(rodada[1][:-1])
        if n_pedro/e > lucas_n1 and n_pedro > lucas_n2:
            lista_resultado.append('Rodada #' + str(cont_rodada) + ': Pedro foi o vencedor')
            pedro_vencidas += 1
        else:
            if lucas_n2*log(lucas_n1) < log(2*pi)/2 + ((n_pedro + 0.5) * log(n_pedro) - n_pedro):
                lista_resultado.append('Rodada #' + str(cont_rodada) + ': Pedro foi o vencedor')
                pedro_vencidas += 1
            else:
                lista_resultado.append('Rodada #' + str(cont_rodada) + ': Lucas foi o vencedor')
                lucas_vencidas += 1


pedro_vencidas = lucas_vencidas = 0
lista_resultado = []
calcular_entradas()
saida()
