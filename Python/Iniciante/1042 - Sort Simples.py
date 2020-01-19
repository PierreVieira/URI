"""
Autor: Pierre Vieira
Data da submissão: 25/01/2019 01:27:27
"""
linha = input().split(" ")
A, B, C = linha
primeiro = a = int(A)
maior = a
menor = a
outro = a
segundo = b = int(B)
if b > maior:
    maior = b
elif b < menor:
    menor = b
elif outro != menor and outro != maior:
    outro = b
terceiro = c = int(C)
if c > maior:
    maior = c
elif c < menor:
    menor = c
elif outro != menor and outro != maior:
    outro = b
print(menor)
if outro == menor or outro == maior:
    outro = a
if outro == menor or outro == maior:
    outro = b
if outro == menor or outro == maior:
    outro = c
print(outro)
print(maior)
print("")
print(primeiro)
print(segundo)
print(terceiro)
