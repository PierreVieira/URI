"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 16:22:50
"""
while True:
    n = int(input())
    if n == 0:
        break
    sequencia = [n]
    while True:
        if n == 1:
            break
        if n % 2 == 1:  # Se for ímpar
            n = n*3 + 1
        else:  # Se for par
            n //= 2
        sequencia.append(n)
    print(max(sequencia))
