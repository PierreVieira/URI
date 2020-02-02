"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 18:11:51
"""
lista_copos = ['A', 'B', 'C']
n = int(input())
copo_inicial = input()
for c in range(n):
    troca = int(input())
    if troca == 1:  # A troca com B
        lista_copos[0], lista_copos[1] = lista_copos[1], lista_copos[0]
    elif troca == 2:  # B troca com C
        lista_copos[1], lista_copos[2] = lista_copos[2], lista_copos[1]
    else:  # A troca com C
        lista_copos[0], lista_copos[2] = lista_copos[2], lista_copos[0]
pos_finded = lista_copos.index(copo_inicial)
if pos_finded == 0:
    print('A')
elif pos_finded == 1:
    print('B')
else:
    print('C')
