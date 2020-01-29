"""
Autor: Pierre Vieira
Data da submissão: 28/01/2020 21:24:03
"""
qtde_casos = 0
while True:
    try:
        numero_voluntarios_que_mergulhou, numero_voluntarios_que_mergulhou_e_retornou = map(int, input().split())
    except EOFError:
        break
    else:
        lista_retornados = list(map(int, input().split()))
        lista_voluntarios = [i + 1 for i in range(numero_voluntarios_que_mergulhou)]
        lista_mortos = list([voluntario for voluntario in lista_voluntarios if not voluntario in lista_retornados])
        if len(lista_mortos) == 0:
            print('*', end='')
        else:
            lista_mortos.sort()
            for morto in lista_mortos:
                print(morto, end=' ')
        print()