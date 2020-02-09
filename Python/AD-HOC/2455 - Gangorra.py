"""
Autor: Pierre Vieira
Data da submissão: 09/02/2020 14:09:21
"""
p1, c1, p2, c2 = map(int, input().split())
mult1, mult2 = p1*c1, p2*c2
if mult1 == mult2:
    print(0)
elif mult1 > mult2:
    print(-1)
else:
    print(1)
