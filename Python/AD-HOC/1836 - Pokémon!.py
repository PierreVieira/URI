"""
Autor: Pierre Vieira
Data da submissão: 26/02/2020 00:17:50
"""
for c in range(int(input())):
    nome_pokemon, level_pokemon = input().split()
    l = float(level_pokemon)
    bs, iv, ev = map(float, input().split())
    hp = int(((iv + bs + (ev ** 0.5) / 8 + 50) * l) / 50 + 10)
    bs, iv, ev = map(float, input().split())
    at = int(((iv + bs + (ev ** 0.5) / 8) * l) / 50 + 5)
    bs, iv, ev = map(float, input().split())
    df = int(((iv + bs + (ev ** 0.5) / 8) * l) / 50 + 5)
    bs, iv, ev = map(float, input().split())
    sp = int(((iv + bs + (ev ** 0.5) / 8) * l) / 50 + 5)
    print('Caso #{}: {} nivel {}'.format(c + 1, nome_pokemon, level_pokemon))
    print('HP: {}\nAT: {}\nDF: {}\nSP: {}'.format(hp, at, df, sp))
