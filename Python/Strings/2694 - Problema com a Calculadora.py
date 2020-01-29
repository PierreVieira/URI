"""
Autor: Pierre Vieira
Data da submissão: 28/01/2020 21:37:18
"""


def retorna_int(string):
    s = ''
    for char in string:
        if char.isnumeric():
            s += char
    return int(s)


for c in range(int(input())):
    string = input()
    s1, s2, s3 = string[2:4], string[5:8], string[11:]
    n1, n2, n3 = retorna_int(s1), retorna_int(s2), retorna_int(s3)
    print(n1 + n2 + n3)
