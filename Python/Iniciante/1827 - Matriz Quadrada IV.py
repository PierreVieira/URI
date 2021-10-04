"""
Autor: Pierre Vieira
Data da submissão: 04/10/2021 18:20:40
"""


def fill_secondary_diagonal(matrix):
    j = 0
    for i in range(len(matrix) - 1, -1, -1):
        matrix[i][j] = 3
        j += 1


def fill_main_diagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 2


def fill_internal(matrix):
    t = len(matrix)
    for i in range(t // 3, t - t // 3):
        for j in range(t // 3, t - t // 3):
            matrix[i][j] = 1


def print_matrix(matrix):
    for line in matrix:
        for number in line:
            print(number, end='')
        print()


def generate_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    half_position = n // 2
    fill_main_diagonal(matrix)
    fill_secondary_diagonal(matrix)
    fill_internal(matrix)
    matrix[half_position][half_position] = 4
    print_matrix(matrix)


while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        generate_matrix(n)
        print()
