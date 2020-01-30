"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 13:50:45
"""
while True:
    linha = input()
    if linha == '0':
        break
    q, d, p = map(int, linha.split())
    quantidade_de_paginas_do_livro = int(p*(q*d)/(p-q))
    if quantidade_de_paginas_do_livro != 1:
        print('{} paginas'.format(quantidade_de_paginas_do_livro))
    else:
        print('{} pagina'.format(quantidade_de_paginas_do_livro))
