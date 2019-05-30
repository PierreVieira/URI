#Pierre Vieira (2473 - Loteria)
def qtde_acertos():
    cont = 0
    for c in aposta:
        if c in sorteio:
            cont += 1
    return cont

aposta = list(map(int, input().split()))
sorteio = list(map(int, input().split()))
if qtde_acertos() == 6:
    print('sena')
elif qtde_acertos() == 5:
    print('quina')
elif qtde_acertos() == 4:
    print('quadra')
elif qtde_acertos() == 3:
    print('terno')
else:
    print('azar')