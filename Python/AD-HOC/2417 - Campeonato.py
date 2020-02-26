"""
Autor: Pierre Vieira
Data da submissão: 25/02/2020 23:51:41
"""
cv, ce, cs, fv, fe, fs = map(int, input().split())
pontos_cormengo = cv*3 + ce
pontos_flamithians = fv*3 + fe
if pontos_cormengo == pontos_flamithians:
    if cs == fs:
        print('=')
    elif cs > fs:
        print('C')
    else:
        print('F')
elif pontos_flamithians > pontos_cormengo:
    print('F')
else:
    print('C')
