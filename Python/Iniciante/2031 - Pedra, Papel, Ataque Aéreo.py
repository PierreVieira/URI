"""
Autor: Pierre Vieira
Data da submissão: 15/02/2020 00:18:56
"""


def solve_this_problem():
    if jogador1 == 'ataque' and jogador2 == 'pedra':
        return 'Jogador 1 venceu'
    elif jogador2 == 'ataque' and jogador1 == 'pedra':
        return 'Jogador 2 venceu'
    elif jogador1 == 'pedra' and jogador2 == 'papel':
        return 'Jogador 1 venceu'
    elif jogador2 == 'pedra' and jogador1 == 'papel':
        return 'Jogador 2 venceu'
    elif jogador1 == 'papel' and jogador2 == 'ataque':
        return 'Jogador 2 venceu'
    elif jogador2 == 'papel' and jogador1 == 'ataque':
        return 'Jogador 1 venceu'
    elif jogador1 == jogador2 == 'papel':
        return 'Ambos venceram'
    elif jogador1 == jogador2 == 'pedra':
        return 'Sem ganhador'
    return 'Aniquilacao mutua'  # jogador1 == jogador2 == 'ataque'


for c in range(int(input())):
    jogador1 = input()
    jogador2 = input()
    print(solve_this_problem())
