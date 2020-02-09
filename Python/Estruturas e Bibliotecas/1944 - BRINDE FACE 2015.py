"""
Autor: Pierre Vieira
Data da submissão: 08/02/2020 22:28:41
"""
lista = ['FACE']
vencedores = 0
for c in range(int(input())):
    lista.append(''.join(input().split()))
    s1, s2 = lista[-1], ''.join((reversed(lista[-2])))
    if s1 == s2:
        lista.pop()
        lista.pop()
        vencedores += 1
    if len(lista) == 0:
        lista.append('FACE')
print(vencedores)