"""
Autor: Pierre Vieira
Data da submissão:
"""
from math import gcd, hypot


def forma_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


while True:
    try:
        a, b, c = sorted(map(int, input().split()))
    except EOFError:
        break
    else:
        if a == 0 or b == 0 or c == 0 or not forma_triangulo(a, b, c):
            print('tripla')
        elif c == hypot(a, b):
            if mdc(a, b) == 1 and mdc(a, c) == 1 and mdc(b, c) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')
