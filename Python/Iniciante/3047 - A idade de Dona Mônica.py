"""
Autor: Pierre Vieira
Data da submissão: 17/01/2020 19:58:46
"""
idade_monica = int(input())
idade_filho1 = int(input())
idade_filho2 = int(input())
idade_filho3 = idade_monica - idade_filho1 - idade_filho2
print(max(idade_filho1, idade_filho2, idade_filho3))
