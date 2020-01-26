"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 17:38:48
"""
from math import factorial
while True:
    entrada = input()
    if entrada == '0':
        break
    qtde_digitos = len(entrada)
    lista_pra_fatorial = [c for c in range(len(entrada), 0, -1)]
    tupla_int = tuple(map(int, tuple(entrada)))
    resultado = 0
    for c in range(qtde_digitos):
        resultado += tupla_int[c]*factorial(lista_pra_fatorial[c])
    print(resultado)