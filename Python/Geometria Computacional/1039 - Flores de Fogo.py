#Ainda não funciona para qualquer entrada, mas terminarei em breve :)

def circulo1_ao_redor_do_circulo2(r1, x1, y1, r2, x2, y2):
    if r1 < r2: #Se o raio do caçador é menor que o raio da flor
        return False
    if x1 == 0 and y1 == 0: #Se o caçador está na origm
        if x2 != 0 or y2 != 0: #Se a flor não está na origm
            return False
    if x2 == 0 and y2 == 0: #Se a flor está na origem
        if x1 != 0 or y1 != 0: #Se a flor não está na origem
            return False
    return True

def mortoOuRico(linha):
    r1, x1, y1, r2, x2, y2 = map(int, linha.split())
    morto = "MORTO"
    rico = "RICO"
    if not circulo1_ao_redor_do_circulo2(r1, x1, y1, r2, x2, y2):
        return morto
    return rico

while True:
    try:
        print(mortoOuRico(input()))
    except EOFError:
        break
