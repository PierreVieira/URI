"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 23:09:21
"""
comprimento_estrada, distancia_entre_pedagios = map(int, input().split())
custo_por_quilometro, valor_pedagio = map(int, input().split())
qtde_pedagios = 0
for c in range(distancia_entre_pedagios, comprimento_estrada+1, distancia_entre_pedagios):
    qtde_pedagios += 1
custo = custo_por_quilometro*comprimento_estrada + qtde_pedagios*valor_pedagio
print(custo)