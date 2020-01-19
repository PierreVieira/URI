"""
Autor: Pierre Vieira
Data da submissão: 16/02/2019 22:02:20
"""
while True:
    string = ''
    linha = input().split(' ')
    x, y = list(map(str, linha))
    lista = []
    if x == y == '0':
        break
    for c in list(y):
        if c != x:
            lista.append(int(c))
    if sum(lista) == 0:
        print('0')
    else:
        for c in lista:
            string += str(c)
        print(int(string))
