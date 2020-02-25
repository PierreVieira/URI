"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 18:54:35
"""
cont = 1
while True:
    try:
        a, b = map(float, input().split())
    except EOFError:
        break
    else:
        print('Projeto {}:'.format(cont))
        print('Percentual dos juros da aplicacao: {:.2f} %\n'.format(100 * ((b - a)/a)))
    cont += 1
