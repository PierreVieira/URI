"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 13:38:32
"""
conjunto_nomes_amigos = set()
conjunto_nomes_nao_amigos = set()
amigo_do_habay = ''
while True:
    linha = input()
    if linha == 'FIM':
        break
    nome, condicao = linha.split()
    if condicao == 'YES':
        conjunto_nomes_amigos.add(nome)
        if len(nome) > len(amigo_do_habay):
            amigo_do_habay = nome
    else:
        conjunto_nomes_nao_amigos.add(nome)
for nome in sorted(conjunto_nomes_amigos):
    print(nome)
for nome in sorted(conjunto_nomes_nao_amigos):
    print(nome)
print('\nAmigo do Habay:\n{}'.format(amigo_do_habay))
