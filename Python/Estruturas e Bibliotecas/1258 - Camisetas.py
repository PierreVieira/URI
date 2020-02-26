"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 14:46:33
"""


def preencher_lista():
    for c in range(n):
        nome = input()
        tipo = input().split()
        if tipo[0] == 'branco':
            if tipo[1] == 'P':
                lista[0][0].append(nome)
            elif tipo[1] == 'M':
                lista[0][1].append(nome)
            else:
                lista[0][2].append(nome)
        else:  # vermelha
            if tipo[1] == 'P':
                lista[1][0].append(nome)
            elif tipo[1] == 'M':
                lista[1][1].append(nome)
            else:
                lista[1][2].append(nome)


def saida_branca():
    for p in sorted(lista[0][0]):
        print('branco P ' + p)
    for m in sorted(lista[0][1]):
        print('branco M ' + m)
    for g in sorted(lista[0][2]):
        print('branco G ' + g)


def saida_vermelha():
    for p in sorted(lista[1][0]):
        print('vermelho P ' + p)
    for m in sorted(lista[1][1]):
        print('vermelho M ' + m)
    for g in sorted(lista[1][2]):
        print('vermelho G ' + g)

cont = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif cont > 0:
        print()
    lista = [[[], [], []], [[], [], []]]  # branco e vermelho. [P, M, G]
    preencher_lista()
    saida_branca()
    saida_vermelha()
    cont += 1
