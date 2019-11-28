from math import cos, sin, pi
from lab4.Sample import Sample
from lab4.functions import prepare_etalon, np


def main():
    sample = Sample()
    sample.print_data()
    A = (sample.Mx1 + sample.Mx2) / 2 - 0.3  # Начало промежутка для генерации критических значений по оси X
    B = (sample.Mx1 + sample.Mx2) / 2 + 0.3  # Конец  промежутка для генерации критических значений по оси X
    C = (sample.My1 + sample.My2) / 2 - 0.3  # Начало промежутка для генерации критических значений по оси Y
    D = (sample.My1 + sample.My2) / 2 + 0.3  # Конец  промежутка для генерации критических значений по оси Y
    z = 50  # кол-во крит. знач на итерацию
    # np.random.seed(1)
    S1 = np.concatenate((sample.Mx1 + sample.SigX1 * np.random.randn(sample.n1, 1),
                         sample.My1 + sample.SigY1 * np.random.randn(sample.n1, 1)),
                        axis=1)
    S2 = np.concatenate((sample.Mx2 + sample.SigX2 * np.random.randn(sample.n2, 1),
                         sample.My2 + sample.SigY2 * np.random.randn(sample.n2, 1)),
                        axis=1)
    prepare_etalon(S1, S2, sample.n1, sample.n2)


def lab4_main(var=1):
    n1 = 19 + var  # Объём первой выборки
    Mx1 = cos(var / 10)  # Мат.ожидание X1
    My1 = sin(var / 10)  # Мат.ожидание Y1
    SigX1 = 0.7 - (var % 10) / 30  # CКО X1
    SigY1 = SigX1  # CКО  Y1
    n2 = 8 + var  # Объём второй выборки
    Mx2 = cos(var / 10 + pi)  # Мат.ожидание X2
    My2 = sin(var / 10 + pi)  # Мат.ожидание Y2
    SigX2 = 0.3 - (var % 10) / 90  # CКО X2
    SigY2 = SigX2  # CКО Y2
    disp1 = SigX1 ** 2
    disp2 = SigX2 ** 2
    print('Выборка')
    print('Объем выборки: %d' % n1)
    print('Мат. ожидание X1: %f' % Mx1)
    print('Мат. ожидание Y1: %f' % My1)
    print("CКО X1 и Y1: %f" % SigX1)
    print('Выборка 2')
    print('Объем выборки: %d' % n2)
    print('Мат. ожидание X1: %f' % Mx2)
    print('Мат. ожидание Y1: %f' % My2)
    print("CКО X1 и Y1: %f" % SigX2)
    A = (Mx1 + Mx2) / 2 - 0.3  # Начало промежутка для генерации критических значений по оси X
    B = (Mx1 + Mx2) / 2 + 0.3  # Конец  промежутка для генерации критических значений по оси X
    C = (My1 + My2) / 2 - 0.3  # Начало промежутка для генерации критических значений по оси Y
    D = (My1 + My2) / 2 + 0.3  # Конец  промежутка для генерации критических значений по оси Y
    z = 50  # кол-во крит. знач на итерацию


main()
