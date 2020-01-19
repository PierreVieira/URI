"""
Autor: Pierre Vieira
Data da submissão: 15/01/2020 23:51:49
"""
n = int(input())
total_preco = 0
total_peso = 0
for c in range(n):
    preco = float(input())
    alimentos = input().split()
    total_preco += preco
    total_peso += len(alimentos)
    print('day {}: {} kg'.format(c+1, len(alimentos)))
print('{:.2f} kg by day\nR$ {:.2f} by day'.format(total_peso/n, total_preco/n))

