"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 17:19:10
"""
while True:
    n = int(input())
    if n == 0:
        break
    cont = 0
    for c in range(1, n+1):
        cont += c**2
    print(cont)
