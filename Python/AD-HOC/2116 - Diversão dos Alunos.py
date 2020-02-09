"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 18:51:27
"""


def prime(x):
    cont = 0
    for c in range(2, int(x ** 0.5 + 1)):
        if x % c == 0:
            cont += 1
    if cont != 0:
        return False
    return True


a, b = map(int, input().split())
lista_a = (i+1 for i in range(a))
lista_b = (i+1 for i in range(b))
for a in lista_a:
    if prime(a):
        p1 = a
for b in lista_b:
    if prime(b):
        p2 = b
print(p1 * p2)
