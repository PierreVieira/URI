"""
Autor: Pierre Vieira
Data da submissão:
"""
from sys import stdin
n = int(input())
lista = list(map(int, stdin.readline().split()))
numero_carneiros = 0
posicao = 0
atacados = [0] * n
total = sum(lista)
tamanho_lista = len(lista)
while True:
    aux = lista[posicao]
    if lista[posicao] > 0:
        numero_carneiros += 1
        lista[posicao] -= 1
        atacados[posicao] = 1
    if aux % 2 == 0:
        posicao -= 1
    else:
        posicao += 1
    if (posicao < 0) or (posicao >= tamanho_lista):
        break
print(sum(atacados), end=' ')
print(total - numero_carneiros)
