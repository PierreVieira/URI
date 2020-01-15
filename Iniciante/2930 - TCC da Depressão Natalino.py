"""
Autor: Pierre Vieira
Data da submissão: 14/01/2020 21:28:22
"""

e, d = map(int, input().split())
dif = d - e
if dif < 0:
    print('Eu odeio a professora!')
elif dif >= 3:
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')
    e += 2
    if e > 23:
        print('Fail! Entao eh nataaaaal!')
    else:
        print('TCC Apresentado!')
