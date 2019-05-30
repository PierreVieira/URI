#Pierre Vieira 29/05/2019
primeira_linha = input().split()
segunda_linha = input().split()
terceira_linha = input().split()
casas = list(map(int, segunda_linha))
entregas = list(map(int, terceira_linha))
minutos = 0
for c in entregas:
    for d in range(len(casas)):
        if(c == casas[d]):
            break
        minutos += 1
print(minutos)