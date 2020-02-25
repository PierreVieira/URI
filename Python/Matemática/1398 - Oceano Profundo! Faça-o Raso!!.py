"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 19:43:04
"""

while True:
    string = ''
    try:
        while True:
            entrada = input()
            string += entrada
            if entrada[-1] == '#':
                break
    except EOFError:
        break
    else:
        string = string[:-1]
        n = int(int(string, 2))
        resto_div = n % 131071
        if resto_div == 0:
            print('YES')
        else:
            print('NO')
