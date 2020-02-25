"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 23:03:11
"""
qtde_candidatos = int(input())
votos_por_candidato = tuple(map(int, input().split()))
total_votos = sum(votos_por_candidato)
maior_voto = max(votos_por_candidato)
relacao_mais_votado = maior_voto/total_votos
if relacao_mais_votado >= 0.45:
    print(1)
elif relacao_mais_votado >= 0.4:
    entrou_no_if = False
    for relacao_voto in map(lambda x: x/total_votos, votos_por_candidato):
        if relacao_mais_votado - relacao_voto <= 0.1 and relacao_mais_votado != relacao_voto:
            print(2)
            entrou_no_if = True
            break
    if not entrou_no_if:
        print(1)
else:
    print(2)