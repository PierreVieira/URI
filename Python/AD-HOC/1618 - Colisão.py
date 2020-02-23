"""
Autor: Pierre Vieira
Data da submissão: 23/02/2020 15:47:38
"""


class Vertice():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Quadrado():
    def __init__(self, vertice_a, vertice_b, vertice_c, vertice_d):
        self._vertice_a = vertice_a
        self._vertice_b = vertice_b
        self._vertice_c = vertice_c
        self._vertice_d = vertice_d

    def colidiu_com_vertice(self, robot):
        """
        :param robot: robô que está sendo analisado.
        :return: True se o robô está colidindo com o quadrado, false caso contrário.
        """
        if robot == self._vertice_a or robot == self._vertice_b or robot == self._vertice_c or robot == self._vertice_d:
            return True
        if self._vertice_a.x <= robot.x <= self._vertice_b.x and self._vertice_a.y <= robot.y <= self._vertice_d.y:
            return True
        return False


for c in range(int(input())):
    ax, ay, bx, by, cx, cy, dx, dy, rx, ry = map(int, input().split())
    quadrado = Quadrado(Vertice(ax, ay), Vertice(bx, by), Vertice(cx, cy), Vertice(dx, dy))
    robo = Vertice(rx, ry)
    if quadrado.colidiu_com_vertice(robo):
        print(1)
    else:
        print(0)
