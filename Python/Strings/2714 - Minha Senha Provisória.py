"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 18:12:09
"""
for c in range(int(input())):
    string = input()
    if len(string) != 20 or string[0:2] != 'RA':
        print('INVALID DATA')
    else:
        print(int(string[2:]))
