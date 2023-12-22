import matplotlib.pyplot as plt
import math
import Link


def findModule(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def findAngle(x, y):
    if y == 0:
        return 0
    return math.atan(x / y)


class Aper(Link.Link):
    name = "Апериодическое звено"

    def __init__(self):
        self.changeK()
        self.changeT()

    def makeStep(self, k, T, e):
        yp = []
        xp = []
        for x in range(0, 100):
            x /= 10
            yp.append(k / (T * x + 1))
            xp.append(x)
        return xp, yp

    def makeAFCH(self, k, T, e):
        yp = []
        xp = []
        for w in range(0, 100):
            w /= 10
            yp.append(-(k * T * w) / ((T * w) ** 2 + 1))
            xp.append(k / ((T * w) ** 2 + 1))
        return xp, yp

    def makeACH(self, k, T, e):
        yp = []
        xp = []
        for w in range(0, 100):
            w /= 10
            y = findModule(k / ((T * w) ** 2 + 1), -(k * T * w) / ((T * w) ** 2 + 1))
            yp.append(y)
            xp.append(w)
        return xp, yp

    def makeFCH(self, k, T, e):
        yp = []
        xp = []
        for w in range(0, 100):
            w /= 10
            y = findAngle(k / ((T * w) ** 2 + 1), -(k * T * w) / ((T * w) ** 2 + 1))
            yp.append(y)
            xp.append(w)
        return xp, yp


ap = Aper()
