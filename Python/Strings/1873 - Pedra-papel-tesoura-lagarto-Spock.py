"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 20:25:02
"""
dict_vitorias = {
    'tesoura': ('papel', 'lagarto'),
    'papel': ('pedra', 'spock'),
    'pedra': ('lagarto', 'tesoura'),
    'lagarto': ('spock', 'papel'),
    'spock': ('tesoura', 'pedra'),
}
for c in range(int(input())):
    sheldon, rajesh = input().split()
    if sheldon == rajesh:
        print('empate')
    else:
        for key, value in dict_vitorias.items():
            if key == sheldon:
                if rajesh in dict_vitorias[key]:
                    print('rajesh')
                else:
                    print('sheldon')
