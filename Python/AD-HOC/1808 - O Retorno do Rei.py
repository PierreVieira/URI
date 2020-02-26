"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 01:59:31
"""
from statistics import mean
notas = []
linha = input()
string_possivel_10 = ''
for c in range(len(linha)):
    if linha[c] != '1' and linha[c] != '0':
        notas.append(int(linha[c]))
    else:
        if linha[c] == '0' and string_possivel_10 == '':
            notas.append(0)
        else:
            if linha[c] == '1':
                if string_possivel_10 == '1':
                    notas.append(1)
                    string_possivel_10 = ''
                string_possivel_10 += '1'
            else:  # linha[c] == 10
                string_possivel_10 += '0'
                notas.append(int(string_possivel_10))
                string_possivel_10 = ''
if len(string_possivel_10) != 0:
    notas.append(int(string_possivel_10))
print('{:.2f}'.format(mean(notas)))
