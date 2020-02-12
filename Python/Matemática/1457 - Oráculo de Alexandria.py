"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 20:06:55
"""


def my_factorial(numero, passo):
    res = 1
    for i in range(numero, 1, -passo):
        res *= i
    return res


for c in range(int(input())):
    n = input()
    numero = int(n[:n.find('!')])
    qtde_exclamacoes = n.count('!')
    print(my_factorial(numero, qtde_exclamacoes))
