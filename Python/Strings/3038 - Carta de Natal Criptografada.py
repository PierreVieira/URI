"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 21:53:10
"""
while True:
    try:
        entrada = input()
    except EOFError:
        break
    else:
        print(entrada.replace('@', 'a').replace('&', 'e').replace('!', 'i').replace('*', 'o').replace('#', 'u'))
