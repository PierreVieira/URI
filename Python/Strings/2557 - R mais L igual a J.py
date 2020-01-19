"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 22:55:52
"""
while True:
    try:
        linha = input()
    except EOFError:
        break
    else:
        if 'J' in linha:
            print(int(linha.split('+')[0]) + int(linha.split('+')[1].split('=')[0]))
        elif 'L' in linha:
            lista = linha.split('+')
            v1 = int(lista[0])
            v2 = int(lista[1].split('=')[-1])
            print(v2 - v1)
        else:  # 'R' in linha
            lista = linha.split('+')
            v1, v2 = map(int, lista[1].split('='))
            print(v2 - v1)
