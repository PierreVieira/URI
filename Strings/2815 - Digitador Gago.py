"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 22:24:54
"""
print(' '.join(map(lambda palavra: palavra[2:] if palavra[:2:] == palavra[2:4:] else palavra, list(input().split()))))
