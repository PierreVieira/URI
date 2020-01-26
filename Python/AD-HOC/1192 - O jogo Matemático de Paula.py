"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 15:38:27
"""
n = int(input())
for c in range(n):
    line = input()
    n1, letra, n2 = int(line[0]), line[1], int(line[2])
    if n1 == n2:
        print(n1*n2)
    elif letra.islower():
        print(n1 + n2)
    else:
        print(n2 - n1)