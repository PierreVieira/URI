"""
Autor: Pierre Vieira
Data da submissão: 12/02/2020 19:42:24
"""

from math import hypot


class Circulo:
    def __init__(self, raio, x_centro, y_centro):
        self.raio = raio
        self.centro = {'x': x_centro, 'y': y_centro}

    def esta_dentro(self, circ):
        """
        Duas circunferências são consideradas internas quando não possuem pontos em comum e uma está localizada no
        interior da outra. A condição para que isso ocorra é que a distância entre os centros das circunferências deve
        ser equivalente à diferença entre as medidas de seus raios.
        :param circ: circunferência que deve englobar self
        :return: True se self está dentro de circ, caso contrário retorna False
        """
        dist_centros = hypot(self.centro['x'] - circ.centro['x'], self.centro['y'] - circ.centro['y'])
        if circ.raio >= dist_centros + self.raio:
            return True
        return False


while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
    except EOFError:
        break
    else:
        cacador = Circulo(r1, x1, y1)
        flor = Circulo(r2, x2, y2)
        if flor.esta_dentro(cacador):
            print('RICO')
        else:
            print('MORTO')
