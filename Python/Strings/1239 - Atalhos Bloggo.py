"""
Autor: Pierre Vieira
Data da submissão: 08/11/2019 13:01:14
"""
def changeHTML(linha):
    string = ""
    primeiro_underline = True
    primeiro_asterisco = True
    for c in linha:
        if c == '_' and primeiro_underline:
            c = "<i>"
            primeiro_underline = not primeiro_underline
        elif c == '_' and not primeiro_underline:
            c = "</i>"
            primeiro_underline = not primeiro_underline
        elif c == '*' and primeiro_asterisco:
            c = "<b>"
            primeiro_asterisco = not primeiro_asterisco
        elif c == '*' and not primeiro_asterisco:
            c = "</b>"
            primeiro_asterisco = not primeiro_asterisco
        string += c
    return string


while True:
    try:
        print(changeHTML(input()))
    except EOFError:
        break
