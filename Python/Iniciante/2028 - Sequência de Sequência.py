"""
Autor: Pierre Vieira
Data da submissão: 02/01/2020 23:21:20
"""


def seq(numero):
    lista = []
    for i in range(numero+1):
        lista.extend([i]*i)
    lista.insert(0, 0)
    return lista


caso = 1
while True:
    try:
        numero = int(input())
    except EOFError:
        break
    else:
        if numero == 0:
            print('Caso {}: 1 numero\n0\n'.format(caso))
        else:
            sequencia = seq(numero)
            print('Caso {}: {} numeros\n{}\n'.format(caso, len(sequencia), str(sequencia)[1:].replace("]", "").replace(",", "")))
        caso += 1