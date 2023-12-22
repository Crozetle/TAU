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
    return math.sqrt(x**2 + y**2)
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

    def stepR(self):
        T = 3
        for k in 1, 3, 5:
            x, y = self.makeStep(k, T)
            plt.plot(x, y, label=f"plot k = {k}", marker='o', markersize=4)
        plt.title("Апериодическое звено - Переходная характеристика - Изменение к")
        plt.legend(("k = 1", "k = 3", "k = 5"))
        plt.savefig("stepR k")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeStep(k, T)
            plt.plot(x, y, label=f"plot k = {k}", marker='o', markersize=4)
        plt.title("Апериодическое звено - Переходная характеристика - Изменение Т")
        plt.legend(("T = 1", "T = 3", "T = 5"))
        plt.savefig("stepR T")
        plt.clf()

    def afch(self):
        T = 3
        for k in 1, 3, 5:
            x, y = self.makeAFCH(k, T)
            plt.plot(x, y, label=f"plot k = {k}", marker='o', markersize=4)
        plt.title("Апериодическое звено - АФЧХ - Изменение к")
        plt.legend(("k = 1", "k = 3", "k = 5"))
        plt.savefig("afch k")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeAFCH(k, T)
            plt.plot(x, y, label=f"plot k = {k}", marker='o', markersize=4)
        plt.title("Апериодическое звено - АФЧХ - Изменение Т")
        plt.legend(("T = 1", "T = 3", "T = 5"))
        plt.savefig("afch T")
        plt.clf()

ap = Aper
ap.stepR()
ap.afch()

