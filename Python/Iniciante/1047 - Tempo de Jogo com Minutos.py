"""
Autor: Pierre Vieira
Data da submissão: 25/01/2019 20:48:37
"""
A, B, C, D = input().split(" ")
a = int(A)
b = int(B)
c = int(C)
d = int(D)
horas = c - a
minutos = d - b
if a == b == c == d:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif horas == -1: # c-a = -1
    if d > b:
        print("O JOGO DUROU 23 HORA(S) E {} MINUTO(S)".format(minutos))
    elif d < b:
        print("O JOGO DUROU 22 HORA(S) E {} MINUTO(S)".format(60 - abs(minutos)))
    else: #b = d
        print("O JOGO DUROU 23 HORA(S) E 0 MINUTO(S)")
elif a > c:
    if d > b:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24 - abs(horas), minutos))
    elif d < b:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24 - abs(horas) - 1,60 - abs(minutos)))
    else: #b = d
        print("O JOGO DUROU {} HORA(S) E 0 MINUTO(S)".format(24 - abs(horas)))
else: # c > a
    if d > b:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
    elif d < b:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas - 1,60 - abs(minutos)))
    else: #b = d
        print("O JOGO DUROU {} HORA(S) E 0 MINUTO(S)".format(horas))
