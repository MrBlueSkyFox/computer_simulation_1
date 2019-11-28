import numpy as np


def prepare_etalon(s1, s2, n1, n2):
    distance = np.zeros(shape=(n1, n2))
    summary_dist = np.zeros(shape=(n1, 1))
    for i in range(0, n1):
        for j in range(0, n2):
            distance[i, j] = np.math.sqrt((s1[i, 0] - s2[j, 0]) ** 2 +
                                          (s1[i, 1] - s2[j, 1]) ** 2)
        summary_dist[i] = sum(distance[i])
    # центр 1-го эталона класса
    max_val = np.amax(summary_dist)
    # max_index = np.where(summary_dist == max_val)
    max_index = np.argmax(summary_dist)
    # центр конкурирующего эталона
    min_val = np.amin(distance[max_index, :])
    # min_index = np.where(distance[max_index[0], :] == min_val)
    min_index = np.argmin(distance[max_index, :])
    # Сформировать множество объектов U
    u = np.zeros([1, 2])
    for i in range(0, n1):
        rroj = np.math.sqrt((s1[max_index, 0] - s1[i, 0]) ** 2 +
                            (s1[max_index, 1] - s1[i, 1]) ** 2)
        rroc = np.math.sqrt((s2[min_index, 0] - s1[i, 0]) ** 2 +
                            (s2[min_index, 1] - s1[i, 1]) ** 2)
        if rroj < rroc and rroj <= min_val:
            print(s1[i])
            a = s1[i]
            u = np.concatenate((u, a))

            # u = np.append(u, s1[i, :], axis=0)
    new_s = np.isin(s1, u)
    new_s2 = np.setdiff1d(s1, u)
    print(new_s)
    print('\n', new_s)


def is_member(A, B):
    return [np.sum(a == B) for a in A]
