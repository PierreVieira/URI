"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 18:54:37
"""
from collections import deque

while True:
    n = int(input())
    removidos = []
    if n == 0:
        break
    deq = deque([c for c in range(n, 0, -1)])
    while n > 1:
        removidos.append(deq.pop())
        deq.appendleft(deq.pop())
        n -= 1
    print('Discarded cards: ' + str(removidos).replace('[', '').replace(']', ''))
    print('Remaining card: ' + str(deq[0]))
