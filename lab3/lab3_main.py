from math import log
import matplotlib.pyplot as plt
# from lab3.side_function import np
import numpy as np
import scipy.special as special
from scipy.stats import chi2
from scipy.special import factorial


# Получить модель пауссоновского потока
def puasson_thread(lambda_value, T1, T2):
    U = []
    T = []
    t = 0
    while t <= T2:
        e = np.random.random()
        u = -log(e) / lambda_value
        U.append(u)
        t = T1 + sum(U)
        T.append(t)
    return U, T


# def hypothesis_testing_2()

def hypothesis_testing(lambda_value, T1, T2, threads, intervals):
    nl = []
    for i in range(0, threads):
        u_i, t_i = puasson_thread(lambda_value, T1, T2)
        # h = matplotlib.pyplot.hist(t_i, intervals)
        n, bins, pathces = plt.hist(x=t_i, bins=intervals)
        nl = np.concatenate((n, nl))
    delta_t = (T2 - T1) / intervals
    unique = np.unique(nl)
    freq = []
    print('Варианты \t Частоты\n')
    for a in unique:
        # freq.append(sum(nl == a))
        freq = np.append(freq, sum(nl == a))
        # print(a, "\t\t", freq[int(a)])
        print('%d\t\t\t%d' % (a, freq[-1]))
    M = sum(unique * freq) / sum(freq)
    print('Выборочное математическое ожидание = ' + str(M) + "\n")
    theoretical_p_pausson = (M ** unique * np.exp(-M)) / factorial(unique)
    theoretical_freq = theoretical_p_pausson * sum(freq)
    print("Варианты\tЧастоты\tТеоретические частоты\n")
    for i in range(0, len(unique)):
        print('%d\t\t\t%d\t\t%f' % (unique[i], freq[i], theoretical_freq[i]))
    hi2 = sum((freq - theoretical_freq) ** 2 / theoretical_freq)
    hi2_teor = chi2.ppf(0.95, intervals - 2)
    print('Хи2 практ. = %f\nХи2 теор. = %f' % (hi2, hi2_teor))
    if hi2 < hi2_teor:
        print('Гипотеза о паусоновском патоке не отклоняется')
    else:
        print('Гипотеза о пасоновском патоке отклоняется')


def hypothesis_testing_2l(lambda_value_1, lambda_value_2, T1, T2, threads, intervals):
    nl = []
    for i in range(0, threads):
        u_1, t_1 = puasson_thread(lambda_value_1, T1, T2)
        u_2, t_2 = puasson_thread(lambda_value_2, T1, T2)
        # h = matplotlib.pyplot.hist(t_i, intervals)
        # d = list.extend(t_1, t_2)
        n, bins, pathces = plt.hist(x=t_1 + t_2, bins=intervals)
        nl = np.concatenate((n, nl))
    delta_t = (T2 - T1) / intervals
    unique = np.unique(nl)
    freq = []
    print('Варианты \t Частоты\n')
    for a in unique:
        # freq.append(sum(nl == a))
        freq = np.append(freq, sum(nl == a))
        # print(a, "\t\t", freq[int(a)])
        print('%d\t\t\t%d' % (a, freq[-1]))
    M = sum(unique * freq) / sum(freq)
    print('Выборочное математическое ожидание = ' + str(M) + "\n")
    theoretical_p_pausson = (M ** unique * np.exp(-M)) / factorial(unique)
    theoretical_freq = theoretical_p_pausson * sum(freq)
    print("Варианты\tЧастоты\tТеоретические частоты\n")
    for i in range(0, len(unique)):
        print('%d\t\t\t%d\t\t%f' % (unique[i], freq[i], theoretical_freq[i]))
    hi2 = sum((freq - theoretical_freq) ** 2 / theoretical_freq)
    hi2_teor = chi2.ppf(0.95, intervals - 2)
    print('Хи2 практ. = %f\nХи2 теор. = %f' % (hi2, hi2_teor))
    if hi2 < hi2_teor:
        print('Гипотеза о паусоновском патоке не отклоняется')
    else:
        print('Гипотеза о пасоновском патоке отклоняется')


def main(N=1):
    T1 = N
    T2 = 100 + N
    lambda1 = (N + 8) / (N + 24)
    lambda2 = (N + 9) / (N + 25)
    print("Вариант: " + str(N) + "\nT1 = " + str(T1) + "\nT2 = " + str(T2) + '\nlambda1 = ' +
          str(lambda1) + "\nlambda2 = " + str(lambda2))
    u_1, t_1 = puasson_thread(lambda1, T1, T2)
    u_2, t_2 = puasson_thread(lambda2, T1, T2)
    fig, ax = plt.subplots()
    # y0, y1, y2, y3 = [], [], [], []
    y0 = np.full((1, len(t_1)), 0)
    y1 = np.full((1, len(t_2)), 1)
    y2 = np.full((1, len(t_1)), 2)
    y3 = np.full((1, len(t_2)), 3)
    ax.scatter(t_1, y0, c='r')
    ax.scatter(t_2, y1, c='b')
    ax.scatter(t_1, y2, c='r')
    ax.scatter(t_2, y3, c='b')
    plt.show()
    print('\nLambda 1 ')
    hypothesis_testing(lambda1, T1, T2, 50, 25)

    print('\nLambda 2 ')
    hypothesis_testing(lambda2, T1, T2, 50, 25)

    print('\nLambda 1 + Lambda 2 ')
    hypothesis_testing(lambda1 + lambda2, T1, T2, 50, 25)

    print('\nX1 +X2')
    hypothesis_testing_2l(lambda1, lambda2, T1, T2, 50, 25)


main(1)
