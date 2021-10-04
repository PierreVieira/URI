"""
Autor: Pierre Vieira
Data da submissão: 04/10/2021 18:34:32
"""

import operator


class Person:
    def __init__(self, name):
        self.name = name
        self.first_letter = name[0]


n = int(input())
persons = [Person(input()) for _ in range(n)]
for person in sorted(persons, key=operator.attrgetter('first_letter')):
    print(person.name)
