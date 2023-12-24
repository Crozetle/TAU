import matplotlib.pyplot as plt


class Link:

    name: str

    def makeStep(self, k, T, e):
        pass
    def makeAFCH(self, k, T, e):
        pass

    def makeACH(self, k, T, e):
        pass

    def makeFCH(self, k, T, e):
        pass

    def changeK(self):
        e = 0.5
        T = 3
        for k in 1, 3, 5:
            x, y = self.makeStep(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - Переходная характеристика - Изменение к")
        plt.legend(("k = 1", "k = 3", "k = 5"))
        plt.savefig(f"{self.name} - Переходная характеристика - Изменение к")
        plt.clf()

        for k in 1, 3, 5:
            x, y = self.makeAFCH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - АФЧХ - Изменение к")
        plt.legend(("k = 1", "k = 3", "k = 5"))
        plt.savefig(f"{self.name} - АФЧХ - Изменение к")
        plt.clf()

        for k in 1, 3, 5:
            x, y = self.makeACH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - АЧХ - Изменение к")
        plt.legend(("k = 1", "k = 3", "k = 5"))
        plt.savefig(f"{self.name} - АЧХ - Изменение к")
        plt.clf()

        for k in 1, 3, 5:
            x, y = self.makeFCH(k, T, e)
            plt.plot(x, y, marker='o', markersize=1)

        plt.title(f"{self.name} - ФЧХ - Изменение к")
        plt.legend(("k = 1", "k = 3", "k = 5"))
        plt.savefig(f"{self.name} - ФЧХ - Изменение к")
        plt.clf()

    def changeT(self):
        e = 0.5
        k = 3
        for T in 1, 3, 5:
            x, y = self.makeStep(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - Переходная характеристика - Изменение T")
        plt.legend(("T = 1", "T = 3", "T = 5"))
        plt.savefig(f"{self.name} - Переходная характеристика - изменение Т")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeAFCH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - АФЧХ - Изменение T")
        plt.legend(("T = 1", "T = 3", "T = 5"))
        plt.savefig(f"{self.name} - АФЧХ - изменение Т")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeACH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - АЧХ - Изменение T")
        plt.legend(("T = 1", "T = 3", "T = 5"))
        plt.savefig(f"{self.name} - АЧХ - изменение Т")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeFCH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - ФЧХ - Изменение T")
        plt.legend(("T = 1", "T = 3", "T = 5"))
        plt.savefig(f"{self.name} - ФЧХ - изменение Т")
        plt.clf()

    def changeE(self):
        k = 3
        T = 3
        for e in 0.2, 0.5, 0.8:
            x, y = self.makeStep(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - Переходная характеристика - Изменение E")
        plt.legend(("E = 1", "E = 3", "E = 5"))
        plt.savefig(f"{self.name} - Переходная характеристика - изменение E")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeAFCH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - АФЧХ - Изменение E")
        plt.legend(("E = 1", "E = 3", "E = 5"))
        plt.savefig(f"{self.name} - АФЧХ - изменение E")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeACH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - АЧХ - Изменение E")
        plt.legend(("E = 1", "E = 3", "E = 5"))
        plt.savefig(f"{self.name} - АЧХ - изменение E")
        plt.clf()

        k = 3
        for T in 1, 3, 5:
            x, y = self.makeFCH(k, T, e)
            plt.plot(x, y, marker='o', markersize=4)

        plt.title(f"{self.name} - ФЧХ - Изменение E")
        plt.legend(("E = 1", "E = 3", "E = 5"))
        plt.savefig(f"{self.name} - ФЧХ - изменение E")
        plt.clf()

    def changeKOnOnePic(self):
        ax = plt.axes()
        f = plt.figure()

        f, ax = plt.subplots(2, 2)
        f.set_size_inches(19.2, 10.8)
        f.set_facecolor("#eee")

        e = 0.5
        T = 3
        for k in 1, 3, 5:
            x, y = self.makeStep(k, T, e)
            ax[0, 0].plot(x, y, marker='o', markersize=4)


        for k in 1, 3, 5:
            x, y = self.makeAFCH(k, T, e)
            ax[0, 1].plot(x, y, marker='o', markersize=4)


        for k in 1, 3, 5:
            x, y = self.makeACH(k, T, e)
            ax[1, 0].plot(x, y, marker='o', markersize=4)


        for k in 1, 3, 5:
            x, y = self.makeFCH(k, T, e)
            ax[1, 1].plot(x, y, marker='o', markersize=1)

        ax[0, 0].set_title("Переходная характеристика")
        ax[0, 0].legend(("k = 1", "k = 3", "k = 5"))

        ax[0, 1].set_title("АФЧХ")
        ax[0, 1].legend(("k = 1", "k = 3", "k = 5"))

        ax[1, 0].set_title("АЧХ")
        ax[1, 0].legend(("k = 1", "k = 3", "k = 5"))

        ax[1, 1].set_title("ФЧХ")
        ax[1, 1].legend(("k = 1", "k = 3", "k = 5"))

        f.suptitle(f"{self.name}")
        f.savefig(f"{self.name} - Изменение к")
        f.clf()

