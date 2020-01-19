"""
Autor: Pierre Vieira
Data da submissão: 10/01/2020 15:19:13
"""
from math import ceil

v, n = map(int, input().split())
res = v * n
list_percent = [i for i in range(10, 91, 10)]
list_float = [res*x/100 for x in list_percent]
list_int = list(map(lambda n: ceil(n), list_float))
print(str(list_int)[1::].strip(']').replace(',', ''))
