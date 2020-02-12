"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 16:59:18
"""


def pega_assinatura(x):
    assinaturas = {}
    for c in range(x):
        nome, assinatura = input().split()
        assinaturas[nome] = assinatura
    return assinaturas


def diferencas(s1, s2):
    """Calcula as diferenças entre s1 e s2"""
    cont = 0
    for c in range(len(s1)):
        if s1[c] != s2[c]:
            cont += 1
    return cont


def qtde_assinaturas_falsas():
    cont = 0
    for nome in assinaturas_do_dia.keys():
        if diferencas(assinaturas_do_dia[nome], originais[nome]) > 1:
            cont += 1
    return cont


while True:
    n = int(input())
    if n == 0:
        break
    originais = pega_assinatura(n)
    m = int(input())
    assinaturas_do_dia = pega_assinatura(m)
    print(qtde_assinaturas_falsas())
