"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 16:19:08
"""
cont = 0
while True:
    cont += 1
    n = int(input())
    if n == 0:
        break
    tupla_numeros = tuple(map(int, input().split()))
    print('Teste {}'.format(cont))
    for c in range(len(tupla_numeros)):
        if tupla_numeros[c] - 1 == c:
            print(c + 1)
            break
    print()
