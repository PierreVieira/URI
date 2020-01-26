"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 14:22:16
"""
while True:
    number_plays = int(input())
    if number_plays == 0:
        break
    plays = tuple(map(int, input().split()))
    print('Mary won {} times and John won {} times'.format(plays.count(0), plays.count(1)))
