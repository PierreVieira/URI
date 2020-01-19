"""
Autor: Pierre Vieira
Data da submissão: 19/01/2019 21:40:31
"""
n_segundos = int(input())
horas = n_segundos//3600
minutos = (n_segundos%3600)//60
segundos = ((n_segundos%3600)%60)
print("{}:{}:{}".format(horas, minutos, segundos))
