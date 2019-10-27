"""
Autor: Pierre Vieira
Data da submissão: 27/01/2019 00:45:36
"""
while True:
    try:
        resultado1 = resultado2 = 1
        linha = input().split(" ")
        A, B = linha
        a = int(A)
        b = int(B)
        for c in range(a, 0, -1):
            resultado1 *= c
        soma = resultado1
        for c in range(b, 0, -1):
            resultado2 *= c
        soma+= resultado2
        print(soma)
    except EOFError:
        break