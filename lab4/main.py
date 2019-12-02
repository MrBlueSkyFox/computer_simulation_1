from math import cos, sin, pi
from lab4.Sample import Sample
from lab4.functions import np, prepare_etalon, etalon, control_element, clean_etalon, FRis_function
import matplotlib.pyplot as plt


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
    u1 = prepare_etalon(S1, S2, sample.n1, sample.n2)
    u2 = prepare_etalon(S2, S1, sample.n2, sample.n1)
    # Находим эталоны
    x01, y01, l1 = etalon(u1)
    x02, y02, l2 = etalon(u2)
    # Генерация контрольных элементов
    c_x1 = control_element(sample.Mx1, sample.SigX1, z)
    c_y1 = control_element(sample.My1, sample.SigY1, z)
    c_x2 = control_element(sample.Mx2, sample.SigX2, z)
    c_y2 = control_element(sample.My2, sample.SigY2, z)

    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    # plt.plot(S1[:, 0], S1[:, 1], color='red', marker='o')
    plt.plot(S1[:, 0], S1[:, 1], 'ro')
    plt.plot(S2[:, 0], S2[:, 1], color='black', marker='o', linestyle='None')
    # Эталоны
    for i in range(0, l1.shape[0]):
        plt.plot(x01[i], y01[i], color='green', marker='*', linestyle='None')
    for i in range(0, l2.shape[0]):
        plt.plot(x02[i], y02[i], color='blue', marker='*', linestyle='None')
    # Очистка эталоново
    x01, y01, l1 = clean_etalon(x01, y01, l1)
    x02, y02, l2 = clean_etalon(x02, y02, l2)
    # print(np.array_equal(x01, _x01))
    # print(np.array_equal(x02, _x02))
    # print(np.array_equal(y02, _y02))
    # print(np.array_equal(y01, _y01))
    # print(np.array_equal(l1, _l1))
    # print(np.array_equal(l2, _l2))

    control_for_1 = []
    control_for_2 = []
    for i in range(0, z):
        control_for_1 = np.append(control_for_1,
                                  FRis_function(x01, y01, x02, y02, c_x1[i], c_y1[i], sample.disp1, sample.disp2))
        control_for_2 = np.append(control_for_2,
                                  FRis_function(x02, y02, x01, y01, c_x2[i], c_y2[i], sample.disp1, sample.disp2))
    plt.figure()
    plt.title('Fig 2')
    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    s1 = [8 * 4 for n in range(0, c_x1.shape[0])]
    s2 = [8 * 4 for n in range(0, c_x1.shape[0])]
    # plt.scatter(c_x1, c_y1, s=s1, c='k', marker='o')
    # plt.scatter(c_x2, c_y2, s=s2, c='r', marker='o')
    plt.plot(c_x1, c_y1, color='black', marker='o', linestyle='None', markersize=6)
    plt.plot(c_x2, c_y2, color='red', marker='o', linestyle='None', markersize=6)

    for i in range(0, l1.shape[0]):
        plt.scatter(x01[i], y01[i], s=l1[i] * 3, c='g', marker='*')
    for i in range(0, l2.shape[0]):
        plt.scatter(x02[i], y02[i], s=l2[i] * 3, c='b', marker='*')


    plt.show()

    # print('x01\n', x01)
    # print('yo1\n', y01)
    # print('l1\n', l1)
    # print('x02\n', x02)
    # print('yo1\n', y02)
    # print('l1\n', l2)


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
