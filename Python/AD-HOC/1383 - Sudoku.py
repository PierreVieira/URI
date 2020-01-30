"""
Autor: Pierre Vieira
Data da submissão: 30/01/2020 15:00:34
"""


class Sudoku:
    def __init__(self, matriz):
        self.matriz = matriz
        self.pequenas_matrizes = self.gerar_lista_de_pequenas_matrizes()
        self.colunas = self.gerar_lista_de_colunas()
        self.padrao = '[1, 2, 3, 4, 5, 6, 7, 8, 9]'
        self.ok = self.analisar()

    def gerar_lista_de_colunas(self):
        lista_colunas = []
        for linha in range(9):
            lista_c = []
            for coluna in range(9):
                lista_c.append(self.matriz[coluna][linha])
            lista_colunas.append(lista_c)
        return lista_colunas

    def analisar_pequenas_matrizes(self):
        for pequena_matriz in self.pequenas_matrizes:
            if self.padrao != str(list(sorted(pequena_matriz))):
                return False
        return True

    def analisar_linhas(self):
        for linha in self.matriz:
            if self.padrao != str(list(sorted(linha))):
                return False
        return True

    def analisar_colunas(self):
        for coluna in self.colunas:
            if self.padrao != str(list(sorted(coluna))):
                return False
        return True

    def gerar_pequena_matriz(self, n):
        matriz_p = []
        if n == 0:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 0, 2, 0, 2
        elif n == 1:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 0, 2, 3, 5
        elif n == 2:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 0, 2, 6, 8
        elif n == 3:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 3, 5, 0, 2
        elif n == 4:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 3, 5, 3, 5
        elif n == 5:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 3, 5, 6, 8
        elif n == 6:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 6, 8, 0, 2
        elif n == 7:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 6, 8, 3, 5
        else:
            linha_inicio, linha_fim, coluna_inicio, coluna_fim = 6, 8, 6, 8
        for linha in range(linha_inicio, linha_fim + 1):
            for coluna in range(coluna_inicio, coluna_fim + 1):
                matriz_p.append(self.matriz[linha][coluna])
        return matriz_p

    def gerar_lista_de_pequenas_matrizes(self):
        lista = list(self.gerar_pequena_matriz(e) for e in range(9))
        return lista

    def analisar(self):
        return self.analisar_colunas() and self.analisar_colunas() and self.analisar_pequenas_matrizes()


def main():
    n = int(input())
    for c in range(n):
        matriz = []
        for d in range(9):
            matriz.append(list(map(int, input().split())))
        sudoku = Sudoku(matriz)
        print('Instancia {}'.format(c + 1))
        if sudoku.ok:
            print('SIM')
        else:
            print('NAO')
        print()


main()
