"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 13:15:23
"""
lista_nomes = []
comportadas = nao_comportadas = 0
for c in range(int(input())):
    comportamento, nome = input().split()
    if comportamento == '+':
        comportadas += 1
    else:
        nao_comportadas += 1
    lista_nomes.append(nome)
for nome in sorted(lista_nomes):
    print(nome)
print('Se comportaram: {} | Nao se comportaram: {}'.format(comportadas, nao_comportadas))
