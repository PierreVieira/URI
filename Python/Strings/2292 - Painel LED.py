"""
Autor: Pierre Vieira
Data da submissão: 02/02/2020 15:55:51
"""


def decidir(elemento):
    if elemento[0] == 'X' and elemento[1] % 2 == 0:
        return 'X'
    elif elemento[0] == 'X' and elemento[1] % 2 == 1:
        return 'O'
    elif elemento[0] == 'O' and elemento[1] % 2 == 0:
        return 'O'
    return 'X'


def solve_this_problem(string, qtde_piscadas):
    lista_qtde_vezes_trocou_de_estado = [qtde_piscadas]
    lista_qtde_vezes_apagou = [qtde_piscadas // 2 if string[0] == 'X' else (qtde_piscadas + 1) // 2]
    for c in range(1, len(string)):
        lista_qtde_vezes_trocou_de_estado.append(lista_qtde_vezes_apagou[c - 1])
        lista_qtde_vezes_apagou.append(lista_qtde_vezes_trocou_de_estado[-1] // 2 if string[c] == 'X' else (lista_qtde_vezes_trocou_de_estado[-1] + 1) // 2)
    correspondencia = tuple(zip(list(string), lista_qtde_vezes_trocou_de_estado))
    return ''.join(list(map(decidir, correspondencia)))


def main():
    for c in range(int(input())):
        linha = input().split()
        inicio, qtde_piscadas = linha[0], int(linha[1])
        print(solve_this_problem(inicio, qtde_piscadas))


main()
