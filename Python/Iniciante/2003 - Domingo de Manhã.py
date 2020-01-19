"""
Autor: Pierre Vieira
Data da submissão: 24/10/2019 23:12:55
"""
def resultado(horas, minutos):
    if horas == 9:
        return 120
    elif horas < 7:
        return 0
    elif 7 <= horas < 8:
        return minutos
    elif horas >= 8:
        return 60 + minutos

while True:
    try:
        horario = input().split(':')
        horas, minutos = map(int, horario)
        print('Atraso maximo: {}'.format(resultado(horas, minutos)))
    except EOFError:
        break
