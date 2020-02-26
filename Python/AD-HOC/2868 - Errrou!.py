"""
Autor: Pierre Vieira
Data da submissão: 25/02/2020 15:30:15
"""
for c in range(int(input())):
    operando1, operador, operando2, sinal, igualdade = input().split()
    op1, op2, ig = map(int, (operando1, operando2, igualdade))
    if operador == '+':
        equivalencia = op1 + op2
    elif operador == '-':
        equivalencia = op1 - op2
    elif operador == 'x' or operador == '*':
        equivalencia = op1 * op2
    else:  # operador == '/'
        equivalencia = op1 // op2
    distancia_equivalencia = abs(equivalencia - ig)
    print('E'+'r'*distancia_equivalencia+'ou!')