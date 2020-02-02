"""
Autor: Pierre Vieira
Data da submissão: 01/02/2020 21:35:10
"""


def resolveu_todos_os_problemas(linha):
    """Verifica se a linha passada como parâmetro resolveu todos os problemas"""
    return len(linha) == linha.count(1)


def condicao1(matriz):
    """1: Ninguém resolveu todos os problemas."""
    for linha in matriz:
        if resolveu_todos_os_problemas(linha):
            return 0
    return 1


def resolvido_por_pelo_menos_uma_pessoa(coluna):
    return coluna.count(1) >= 1


def gerar_colunas(matriz):
    """Vai gerar uma lista com as colunas da matriz"""
    colunas_matriz = []
    for d in range(qtde_problemas):
        coluna_matriz = []
        for c in range(len(matriz)):
            coluna_matriz.append(matriz[c][d])
        colunas_matriz.append(coluna_matriz.copy())
    return colunas_matriz


def condicao2(matriz):
    """Todo problema foi resolvido por pelo menos uma pessoa(não necessariamente a mesma)."""
    for coluna in gerar_colunas(matriz):
        if not resolvido_por_pelo_menos_uma_pessoa(coluna):
            return 0
    return 1


def problema_resolvido_por_todos(coluna):
    """Verifica se a coluna passada como parâmetro tem todas as questões resolvidas por todos"""
    return coluna.count(1) == len(coluna)


def condicao3(matriz):
    """Não há nenhum problema resolvido por todos"""
    colunas_matriz = gerar_colunas(matriz)
    for coluna in colunas_matriz:
        if problema_resolvido_por_todos(coluna):
            return 0
    return 1


def resolveu_ao_menos_um_problema(linha):
    """Verifica se a linha (jogador) resolveu ao menos um problema"""
    return linha.count(1) >= 1


def condicao4(matriz):
    for linha in matriz:
        if not resolveu_ao_menos_um_problema(linha):
            return 0
    return 1


def solve_this_problem():
    matriz = [list(map(int, input().split())) for c in range(qtde_participantes)]
    c1, c2, c3, c4 = condicao1(matriz), condicao2(matriz), condicao3(matriz), condicao4(matriz)
    return c1 + c2 + c3 + c4


while True:
    qtde_participantes, qtde_problemas = map(int, input().split())
    if qtde_participantes == qtde_problemas == 0:
        break
    print(solve_this_problem())
