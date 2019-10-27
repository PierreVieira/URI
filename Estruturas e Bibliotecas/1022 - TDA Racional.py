"""
Autor: Pierre Vieira
Data da submissão: 01/03/2019 23:38:35
"""
def operar(*dicionario):
    numerador1 = int(dicionario[0])
    numerador2 = int(dicionario[3])
    denominador1 = int(dicionario[1])
    denominador2 = int(dicionario[4])
    sinal = dicionario[2]
    if sinal == '+':
        d = denominador1*denominador2
        n = numerador1*(d/denominador1) + numerador2*(d/denominador2)
    elif sinal == '-':
        d = denominador1*denominador2
        n = numerador1*(d/denominador1) - numerador2*(d/denominador2)
    elif sinal == '*':
        n = numerador2*numerador1
        d = denominador2*denominador1
    else:
        n = numerador1*denominador2
        d = numerador2*denominador1
    return str(int(n)) + '/' + str(int(d))

def mdc(n1, n2):
    if n1 > n2:
        aux = n2
        n2 = n1
        n1 = aux
    while n2 % n1 != 0:
        aux = n2
        n2 = n1
        n1 = aux % n1
    return n1


def simplificar(r):
    lista = r.split('/')
    n = int(lista[0])
    d = int(lista[-1])
    aux = n
    n = n/mdc(n, d)
    d = d/mdc(aux, d)
    if d < 0 and n < 0:
        n = abs(n)
        d = abs(d)
    elif d < 0:
        n *= -1
        d = abs(d)
    return str(int(n))+'/'+str(int(d))

n = int(input())
while n > 0:
    n -= 1
    conta = input().split()
    dicionario = {}
    n1 = conta[0]
    d1 = conta[2]
    sinal = conta[3]
    n2 = conta[4]
    d2 = conta[6]
    resultado = operar(n1, d1, sinal, n2, d2)
    print('{} = {}'.format(resultado, simplificar(resultado)))