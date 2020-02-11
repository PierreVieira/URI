"""
Autor: Pierre Vieira
Data da submissão: 11/02/2020 15:19:36
"""


class Robo:
    def __init__(self, posicao_inicial, orientacao, cenario):
        self.posicao = {'x': posicao_inicial[0], 'y': posicao_inicial[1]}
        self.orientacao = orientacao
        self.cenario = cenario
        self.celulas_coletadas = 0

    def __movimentar_para_frente(self):
        self.posicao['x'] -= 1

    def __movimentar_para_tras(self):
        self.posicao['x'] += 1

    def __movimentar_para_direita(self):
        self.posicao['y'] += 1

    def __movimentar_para_esquerda(self):
        self.posicao['y'] -= 1

    def __coletar_celula(self):
        self.celulas_coletadas += 1

    def __virar_para_direita(self):
        if self.orientacao == 'N':
            self.orientacao = 'L'
        elif self.orientacao == 'O':
            self.orientacao = 'N'
        elif self.orientacao == 'S':
            self.orientacao = 'O'
        else:
            self.orientacao = 'S'

    def __virar_para_esquerda(self):
        if self.orientacao == 'N':
            self.orientacao = 'O'
        elif self.orientacao == 'O':
            self.orientacao = 'S'
        elif self.orientacao == 'S':
            self.orientacao = 'L'
        else:
            self.orientacao = 'N'

    def __movimentacao_livre(self):
        if self.orientacao == 'N':
            if self.posicao['x'] - 1 == -1:
                return False
            elif self.cenario[self.posicao['x'] - 1][self.posicao['y']] == '#':
                return False
        elif self.orientacao == 'S':
            if self.posicao['x'] + 1 == n:
                return False
            elif self.cenario[self.posicao['x'] + 1][self.posicao['y']] == '#':
                return False
        elif self.orientacao == 'L':
            if self.posicao['y'] + 1 == m:
                return False
            elif self.cenario[self.posicao['x']][self.posicao['y'] + 1] == '#':
                return False
        elif self.orientacao == 'O':
            if self.posicao['y'] - 1 == -1:
                return False
            elif self.cenario[self.posicao['x']][self.posicao['y'] - 1] == '#':
                return False
        return True

    def movimentar_robo(self, instructions):
        for instrucao in instructions:
            if instrucao == 'D':
                self.__virar_para_direita()
            elif instrucao == 'E':
                self.__virar_para_esquerda()
            else:  # Instrução == 'F'
                if self.__movimentacao_livre():
                    posicao_anterior = self.posicao.copy()
                    if self.orientacao == 'N':
                        self.__movimentar_para_frente()
                    elif self.orientacao == 'S':
                        self.__movimentar_para_tras()
                    elif self.orientacao == 'L':
                        self.__movimentar_para_direita()
                    elif self.orientacao == 'O':
                        self.__movimentar_para_esquerda()
                    if self.cenario[self.posicao['x']][self.posicao['y']] == '*':
                        self.celulas_coletadas += 1
                    self.cenario[posicao_anterior['x']][posicao_anterior['y']], self.cenario[self.posicao['x']][self.posicao['y']] = '.', self.orientacao


def identifica_posicao_inicial():
    for c in range(n):
        for d in range(m):
            if matriz[c][d] != '*' and matriz[c][d] != '#' and matriz[c][d] != '.':
                return (c, d), matriz[c][d]
    return None


def solve_this_problem():
    posicao_inicial_robo, orientacao = identifica_posicao_inicial()
    robo = Robo(posicao_inicial_robo, orientacao, matriz)
    robo.movimentar_robo(instrucoes)
    return robo.celulas_coletadas


while True:
    n, m, s = map(int, input().split())
    if n == m == s == 0:
        break
    matriz = [list(input()) for c in range(n)]
    instrucoes = input()
    print(solve_this_problem())
