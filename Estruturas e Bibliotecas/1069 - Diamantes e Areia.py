n = int(input())
for k in range(n):
    entrada = list(input())
    qtde_diamante = 0
    for c in range(len(entrada)):
        if entrada[c] == '<':
            for d in range(c, len(entrada)):
                if entrada[d] == '>':
                    entrada[d] = 0
                    qtde_diamante += 1
                    break
    print(qtde_diamante)