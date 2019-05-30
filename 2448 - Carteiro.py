#Pierre Vieira 29/05/2019 - Ainda temos que resolver
primeira_linha = input().split()
segunda_linha = input().split()
terceira_linha = input().split()
casas = list(map(int, segunda_linha))
entregas = list(map(int, terceira_linha))
minutos = 0
for c in entregas:
    for d in casas:
        if c != d:
            minutos += 1
print(int(minutos/2))
