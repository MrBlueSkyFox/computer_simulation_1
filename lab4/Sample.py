from math import cos, sin, pi


class Sample:

    def __init__(self, var=1):
        self.n1 = 19 + var  # Объём первой выборки
        self.Mx1 = cos(var / 10)  # Мат.ожидание X1
        self.My1 = sin(var / 10)  # Мат.ожидание Y1
        self.SigX1 = 0.7 - (var % 10) / 30  # CКО X1
        self.SigY1 = self.SigX1  # CКО  Y1
        self.n2 = 8 + var  # Объём второй выборки
        self.Mx2 = cos(var / 10 + pi)  # Мат.ожидание X2
        self.My2 = sin(var / 10 + pi)  # Мат.ожидание Y2
        self.SigX2 = 0.3 - (var % 10) / 90  # CКО X2
        self.SigY2 = self.SigX2  # CКО Y2
        self.disp1 = self.SigX1 ** 2
        self.disp2 = self.SigX2 ** 2

    def print_data(self):
        print('Выборка')
        print('Объем выборки: %d' % self.n1)
        print('Мат. ожидание X1: %f' % self.Mx1)
        print('Мат. ожидание Y1: %f' % self.My1)
        print("CКО X1 и Y1: %f" % self.SigX1)
        print('Выборка 2')
        print('Объем выборки: %d' % self.n2)
        print('Мат. ожидание X1: %f' % self.Mx2)
        print('Мат. ожидание Y1: %f' % self.My2)
        print("CКО X1 и Y1: %f" % self.SigX2)
