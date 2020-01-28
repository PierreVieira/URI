"""
Autor: Pierre Vieira
Data da submissão: 27/01/2020 22:59:11
"""


def tem_substring_com_o_tamanho(tamanho_pesquisa, s1, s2, t2):
    string_pesquisa = ''
    for i in range(t2):
        j = i
        for k in range(tamanho_pesquisa):
            try:
                string_pesquisa += s2[j]
            except IndexError:
                return False
            else:
                j += 1
        if len(string_pesquisa) != tamanho_pesquisa:
            return False
        elif string_pesquisa in s1:
            return True
        string_pesquisa = ''
    return False


def maior_ocorrencia_s2_em_s1(s1, s2, tamanho_s2):
    maior_tamanho = 0
    for c in range(1, tamanho_s2 + 1):
        if not tem_substring_com_o_tamanho(c, s1, s2, tamanho_s2):
            break
        else:
            maior_tamanho = c
    return maior_tamanho


def maior_ocorrencia(s1, s2):
    """Calcula o tamanho da maior substring comum entre as duas strings informadas"""
    tamanho_s1, tamanho_s2 = len(s1), len(s2)
    if tamanho_s1 > tamanho_s2:
        return maior_ocorrencia_s2_em_s1(s1, s2, tamanho_s1)
    return maior_ocorrencia_s2_em_s1(s2, s1, tamanho_s2)


def main():
    while True:
        try:
            string1 = input()
            string2 = input()
        except EOFError:
            break
        else:
            print(maior_ocorrencia(string1, string2))


main()
