"""
Autor: Pierre Vieira
Data da submissão: 25/10/2019 13:19:22
"""
def todos_os_valores_maiores_que127(valores):
    for c in valores:
        if c <= 127:
            return False
    return True


def valores_iguais_menores_que127(valores):
    lista = []
    for c in valores:
        if c < 127:
            lista.append(c)
    for c in range(len(lista)):
        for d in range(c+1, len(lista), 1):
            if lista[c] == lista[d]:
                return True
    return False


def mais_de_um_menor_que_igual127(valores):
    cont = 0
    for c in valores:
        if c <= 127:
            cont += 1
    if cont > 1:
        return True
    return False


def esta_de_acordo(*valores):
    if todos_os_valores_maiores_que127(valores):
        return False
    elif valores_iguais_menores_que127(valores):
        return False
    elif mais_de_um_menor_que_igual127(valores):
        return False
    return True


def minimo_alternativa(*valores):
    minimo_alternativa = min(valores)
    for c in range(len(valores)):
        if valores[c] == minimo_alternativa:
            if c == 0:
                return "A"
            elif c == 1:
                return "B"
            elif c == 2:
                return "C"
            elif c == 3:
                return "D"
            else:
                return "E"

while True:
        qtde_entradas = int(input())
        if qtde_entradas == 0:
            break
        while qtde_entradas > 0:
            qtde_entradas -= 1
            linha = input().split()
            a, b, c, d, e = map(int, linha)
            if not(esta_de_acordo(a, b, c, d, e)):
                print("*")
            else:
                print(minimo_alternativa(a, b, c, d, e))
