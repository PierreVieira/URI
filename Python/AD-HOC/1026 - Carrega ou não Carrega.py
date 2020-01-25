"""
Autor: Pierre Vieira
Data da submissão: 22/02/2019 17:47:29
"""
while True:
    try:
        linha = input().split()
        n1, n2 = list(map(int, linha))
        print(int(n1 ^ n2))  # Operador ^ é uma xor em python
    except EOFError:
        break
