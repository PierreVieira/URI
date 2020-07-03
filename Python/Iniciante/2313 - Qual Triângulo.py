a, b, c = map(int, input().split())


def valido():
    return a < b + c and b < a + c and c < a + b


def retangulo(maior, menor1, menor2):
    return 'S' if maior**2 == menor1**2 + menor2**2 else 'N'


def tipo_triangulo():
    if a == b == c:
        return 'Valido-Equilatero'
    elif a != b and a != c and b != c:
        return 'Valido-Escaleno'
    return 'Valido-Isoceles'


if valido():
    print(tipo_triangulo())
    ordenado = list(sorted([a, b, c], reverse=True))
    print('Retangulo: {}'.format(retangulo(ordenado[0], ordenado[1], ordenado[2])))
else:
    print('Invalido')
