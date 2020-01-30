"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 15:04:54
"""
while True:
    try:
        sequencia, sequencia_resistente = input(), input()
    except EOFError:
        break
    else:
        if sequencia_resistente in sequencia:
            print('Resistente')
        else:
            print('Nao resistente')
