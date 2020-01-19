"""
Autor: Pierre Vieira
Data da submissão: 19/01/2020 18:02:56
"""
while True:
    n1, n2 = map(int, input().split())
    if n1 == n2 == 0:
        break
    soma = n1 + n2
    for caractere in str(soma):
        if caractere != '0':
            print(caractere, end='')
    print()