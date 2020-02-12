"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 17:52:16
"""


class Jogo():
    def __init__(self):
        self.__qtde_gols_azul = 0
        self.__qtde_gols_verde = 0
        self.__qtde_gols_vermelho = 0

    def vencedor(self):
        if self.__qtde_gols_azul > self.__qtde_gols_verde and self.__qtde_gols_azul > self.__qtde_gols_vermelho:
            return 'blue'
        elif self.__qtde_gols_vermelho > self.__qtde_gols_azul and self.__qtde_gols_vermelho > self.__qtde_gols_verde:
            return 'red'
        elif self.__qtde_gols_verde > self.__qtde_gols_vermelho and self.__qtde_gols_verde > self.__qtde_gols_azul:
            return 'green'
        elif self.__qtde_gols_azul == self.__qtde_gols_verde == self.__qtde_gols_vermelho:
            return 'trempate'
        return 'empate'

    def fez_gol(self, quem_fez, quem_tomou):
        if quem_fez == 'B':
            if quem_tomou == 'R':
                self.__qtde_gols_azul += 2
            else:
                self.__qtde_gols_azul += 1
        elif quem_fez == 'G':
            if quem_tomou == 'B':
                self.__qtde_gols_verde += 2
            else:
                self.__qtde_gols_verde += 1
        else:  # Vermelho fez o gol
            if quem_tomou == 'G':
                self.__qtde_gols_vermelho += 2
            else:
                self.__qtde_gols_vermelho += 1


for c in range(int(input())):
    jogo = Jogo()
    for d in range(int(input())):
        fez, tomou = input().split()
        jogo.fez_gol(fez, tomou)
    print(jogo.vencedor())
