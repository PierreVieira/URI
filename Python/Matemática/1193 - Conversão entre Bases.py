"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 22:21:07
"""
for c in range(int(input())):
    numero, base = input().split()
    print('Case {}:'.format(c + 1))
    if base == 'bin':
        print('{} dec'.format(int(numero, 2)))
        print('{} hex'.format(str(hex(int(str(bin(int(numero, 2)))[2:], 2)))[2:]))
    elif base == 'dec':
        print('{} hex'.format(str(hex(int(numero)))[2:]))
        print('{} bin'.format(str(bin(int(numero)))[2:]))
    else:
        print('{} dec'.format(int(numero, 16)))
        print('{} bin'.format(str(bin(int(numero, 16)))[2:]))
    print()
