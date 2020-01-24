"""
Autor: Pierre Vieira
Data da submissão: 24/01/2020 15:02:01
"""


from functools import lru_cache


@lru_cache(200)
def chamadas(n):
    if n == 1:
        return 0
    elif n == 2:
        return 2
    return chamadas(n - 1) + chamadas(n - 2) + 2


@lru_cache(200)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


qtde_testes = int(input())
for c in range(qtde_testes):
    n = int(input())
    print('fib({}) = {} calls = {}'.format(n, chamadas(n), fib(n)))
