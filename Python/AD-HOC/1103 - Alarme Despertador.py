"""
Autor: Pierre Vieira
Data da submissão: 21/01/2020 18:46:47
"""


from datetime import datetime

while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == m1 == h2 == m2 == 0:
        break
    d = datetime.now()
    data_1 = d.replace(hour=h1, minute=m1)
    data_2 = d.replace(hour=h2, minute=m2)
    tempo = data_2 - data_1  # time delta
    print(tempo.seconds//60)
