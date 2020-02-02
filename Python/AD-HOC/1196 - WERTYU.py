"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 16:48:12
"""
linha = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,.'"
while True:
    s = ''
    try:
        frase = input()
    except EOFError:
        break
    else:
        for c in frase:
            if c == ' ':
                s += c
            else:
                s += linha[linha.find(c)-1]
        print(s)
