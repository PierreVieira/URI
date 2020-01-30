"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 17:46:57
"""
for c in range(int(input())):
    string = input()
    s = ''
    for char in reversed(string):
        if char.islower():
            s += char
    print(s)
