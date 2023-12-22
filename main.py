import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import math


class Link:

    def stepR(self):
        pass

    def ACH(self):
        pass

    def FCH(self):
        pass

    def AFCH(self):
        pass


def findModule(x, y):
    return math.sqrt(x ** 2 + y ** 2)


class Aper:

    def makeStep(self, k, T):
        yp = []
        xp = []
        for x in range(0, 100):
            x /= 10
            yp.append(k / (T * x + 1))
            xp.append(x)
        return xp, yp

    def makeAFCH(self, k, T):
        yp = []
        xp = []
        for w in range(0, 100):
            w /= 10
            yp.append(-(k * T * w) / ((T * w) ** 2 + 1))
            xp.append(k / ((T * w) ** 2 + 1))
        return xp, yp

    def makeACH(self, k, T):
        yp = []
        xp = []
        for w in range(0, 100):
            w /= 10
            y = findModule(k / ((T * w) ** 2 + 1), -(k * T * w) / ((T * w) ** 2 + 1))
            yp.append(y)
            xp.append(w)
        return xp, yp

    def changeK(self):
        T = 3
        for k in 1, 3, 5:
            x, y = self.makeStep(k, T)
            plt1.plot(x, y, label=f"plot k = {k}", marker='o', markersize=4)
            x, y = self.makeAFCH(k, T)
            plt2.plot(x, y, label=f"plot k = {k}", marker='o', markersize=4)
            x, y = self.makeACH(k, T)
            plt3.plot(x, y, label=f"plot k = {k}", marker='o', markersize=4)

        plt1.title("Апериодическое звено - Переходная характеристика - Изменение к")
        plt1.legend(("k = 1", "k = 3", "k = 5"))
        plt1.savefig("Переходная характеристика - К")
        plt1.clf()

        plt2.title("Апериодическое звено - АФЧХ - Изменение к")
        plt2.legend(("k = 1", "k = 3", "k = 5"))
        plt2.savefig("АФЧХ - К")
        plt2.clf()

        plt3.title("Апериодическое звено - АЧХ - Изменение к")
        plt3.legend(("k = 1", "k = 3", "k = 5"))
        plt3.savefig("АЧХ - К")
        plt3.clf()

    def changeT(self):
        k = 3
        for T in 1, 3, 5:
            x, y = self.makeStep(k, T)
            plt1.plot(x, y, label=f"plot T = {k}", marker='o', markersize=4)
            x, y = self.makeAFCH(k, T)
            plt2.plot(x, y, label=f"plot T = {k}", marker='o', markersize=4)
            x, y = self.makeACH(k, T)
            plt3.plot(x, y, label=f"plot T = {k}", marker='o', markersize=4)

        plt1.title("Апериодическое звено - Переходная характеристика - Изменение T")
        plt1.legend(("T = 1", "T = 3", "T = 5"))
        plt1.savefig("Переходная характеристика - T")
        plt1.clf()

        plt2.title("Апериодическое звено - АФЧХ - Изменение T")
        plt2.legend(("T = 1", "T = 3", "T = 5"))
        plt2.savefig("АФЧХ - T")
        plt2.clf()

        plt3.title("Апериодическое звено - АЧХ - Изменение T")
        plt3.legend(("T = 1", "T = 3", "T = 5"))
        plt3.savefig("АЧХ - T")
        plt3.clf()


Aper.changeT(Aper)
Aper.changeK(Aper)
