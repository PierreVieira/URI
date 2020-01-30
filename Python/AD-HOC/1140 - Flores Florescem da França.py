"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 13:29:29
"""
while True:
    linha = input()
    if linha == '*':
        break
    lista_linha = linha.split()
    string = ''.join([palavra[0].lower() for palavra in lista_linha])
    if string.count(string[0])/len(string) == 1:
        print('Y')
    else:
        print('N')
