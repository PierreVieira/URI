"""
Autor: Pierre Vieira
Data da submissão: 17/01/2019 01:13:31
"""
tempo = float(input())
v_media = float(input())
distancia = float(tempo*v_media)
gasto = float(distancia/12)
print("{:.3f}".format(gasto))
