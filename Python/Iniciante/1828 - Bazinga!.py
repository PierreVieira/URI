"""
Autor: Pierre Vieira
Data da submissão: 13/02/2020 01:52:05
"""
dicionario = {
    'tesoura': ('papel', 'lagarto'),
    'papel': ('pedra', 'Spock'),
    'pedra': ('lagarto', 'tesoura'),
    'lagarto': ('Spock', 'papel'),
    'Spock': ('tesoura', 'pedra')
}


def solve_this_problem():
    if sheldon == raj:
        return 'De novo!'
    elif raj in dicionario[sheldon]:
        return 'Bazinga!'
    return 'Raj trapaceou!'


for c in range(int(input())):
    sheldon, raj = input().split()
    print('Caso #{}:'.format(c + 1), end=' ')
    print(solve_this_problem())
