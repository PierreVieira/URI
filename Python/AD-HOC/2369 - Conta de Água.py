"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 17:20:21
"""
n = int(input())


def find1():
    pay = 1 * (n - 10)
    if pay > 20:
        pay = 20
    return pay


def find2():
    pay = 2 * (n - 30)
    if pay > 140:
        pay = 140
    return pay


def find3():
    return 5 * (n - 100)


p1, p2, p3 = find1(), find2(), find3()
if p1 < 0:
    p1 = 0
if p2 < 0:
    p2 = 0
if p3 < 0:
    p3 = 0
print(7 + p1 + p2 + p3)
