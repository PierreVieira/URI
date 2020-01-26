"""
Autor: Pierre Vieira
Data da submissão:
"""
while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        for codigo in sorted(input() for c in range(n)):
            print(codigo)
