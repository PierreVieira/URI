"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 15:57:17
"""


def verifica():
    for c in range(len(line1)):
        if not(line1[c] == '0' and line2[c] == '1' or line2[c] == '0' and line1[c] == '1'):
            return 'N'
    return 'Y'


line1 = input().split()
line2 = input().split()
print(verifica())
