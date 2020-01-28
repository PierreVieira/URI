"""
Autor: Pierre Vieira
Data da submissão: 27/01/2020 23:13:31
"""
for c in range(int(input())):
    inicio, fim = map(int, input().split())
    lista = [str(i) for i in range(inicio, fim+1)]
    lista.extend(list(map(lambda string: string[::-1], reversed(lista))))
    print(''.join(lista))
