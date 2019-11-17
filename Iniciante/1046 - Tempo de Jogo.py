"""
Autor: Pierre Vieira
Data da submissão: 24/01/2019 20:42:12
"""
linha = input().split(" ")
a, b = linha
hora_inicial = int(a)
hora_final = int(b)
if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
elif hora_final == hora_inicial:
    duracao = 24
else:
    cont = 0
    for c in range(hora_inicial, 24):
        cont+=1
    duracao = cont + hora_final
print("O JOGO DUROU {} HORA(S)".format(duracao))
