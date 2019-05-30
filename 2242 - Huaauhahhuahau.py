#Pierre Vieira (2242 - Huaauhahhuahau)
def tem_seguido(lista):
    for c in range(len(lista)):
        if c == 0:
            primeiro = lista[c]
        else:
            primeiro = segundo
        if(c+1 == len(lista)):
            break
        segundo = lista[c+1]
        if primeiro == segundo:
            return True
    return False

def analise(vogais):
    lista = []
    for c in vogais:
        lista.append(c)
        if len(lista) > 1:
            if tem_seguido(lista):
                return True
    return False

def remove_consoantes(string):
    vogais = 'aeiou'
    somente_vogais = []
    for c in string:
        if c in vogais:
            somente_vogais.append(c)
    return ''.join(somente_vogais)

string = input()
apenas_vogais = remove_consoantes(string)
if len(apenas_vogais) == 1:
    print('S')
elif analise(apenas_vogais):
    print('S')
else:
    print('N')