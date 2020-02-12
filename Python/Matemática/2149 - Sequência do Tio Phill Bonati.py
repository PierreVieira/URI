"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 20:32:16
"""
from functools import lru_cache


@lru_cache(300)
def my_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return my_fib(n - 1) * my_fib(n - 2)
    if n % 2 == 1:
        return my_fib(n - 1) + my_fib(n - 2)


while True:
    try:
        numero = int(input())
    except EOFError:
        break
    else:
        print(my_fib(numero))
