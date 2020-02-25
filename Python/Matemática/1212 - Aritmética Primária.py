"""
Autor: Pierre Vieira
Data da submissão: 24/02/2020 21:43:52
"""


def contar_carry(n1, n2):
    carry = qtde_carry = 0
    counter = 1
    while n1 != 0 or n2 != 0:
        ultimo_digito_n1 = int(str(n1)[-1])
        ultimo_digito_n2 = int(str(n2)[-1])
        soma = carry + ultimo_digito_n1 + ultimo_digito_n2
        if soma >= 10:
            carry = int(str(soma)[:-1])
            qtde_carry += 1
        else:
            carry = 0
        n1 //= 10
        n2 //= 10
        counter += 1
    return qtde_carry


while True:
    n1, n2 = map(int, input().split())
    if n1 == n2 == 0:
        break
    qtde_carry = contar_carry(n1, n2)
    if qtde_carry == 0:
        print('No carry operation.')
    elif qtde_carry == 1:
        print('1 carry operation.')
    else:
        print('{} carry operations.'.format(qtde_carry))
