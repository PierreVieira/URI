"""
Autor: Pierre Vieira
Data da submissão: 18/02/2020 08:47:06
"""
while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        lista_pessoas = []
        for c in range(n):
            nome, orientacao, custo = input().split()
            lista_pessoas.append((int(custo), orientacao, nome))
        lista_pessoas.sort()
        for p in lista_pessoas:
            print(p[2])

