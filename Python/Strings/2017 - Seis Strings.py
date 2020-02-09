"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 14:27:45
"""


def encontra_distancia(palavra: str):
    distancia = 0
    for c in range(len(palavra)):
        if palavra[c] != string[c]:
            distancia += 1
    return distancia


string = input()
k = int(input())
strings = [input() for c in range(5)]
distancias = map(encontra_distancia, strings)
menor = min(distancias)
if menor > k:
    print(-1)
else:
    for p in strings:
        if encontra_distancia(p) == menor:
            print(strings.index(p)+1)
            break
    print(encontra_distancia(strings[0]))
