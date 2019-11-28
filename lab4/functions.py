import numpy as np


def prepare_etalon(s1, s2, n1, n2):
    # distance = np.zeros(shape=(n1, n2))
    # summary_dist = np.zeros(shape=(n1, 1))
    # for i in range(0, n1):
    #     for j in range(0, n2):
    #         distance[i, j] = np.math.sqrt((s1[i, 0] - s2[j, 0]) ** 2 +
    #                                       (s1[i, 1] - s2[j, 1]) ** 2)
    #     summary_dist[i] = sum(distance[i])
    distance, summary_dist = calc_dist(n1, n2, s1, s2)
    # # центр 1-го эталона класса
    # max_val = np.amax(summary_dist)
    # max_index = np.argmax(summary_dist)
    # # центр конкурирующего эталона
    # min_val = np.amin(distance[max_index, :])
    # min_index = np.argmin(distance[max_index, :])
    max_val, max_index, min_val, min_index = find_min_max(distance, summary_dist)
    # Сформировать множество объектов U
    u = create_array_etalon(n1, s1, s2, max_index, min_index, min_val)
    # u = np.zeros([1, 2])
    # for i in range(0, n1):
    #     rroj = np.math.sqrt((s1[max_index, 0] - s1[i, 0]) ** 2 +
    #                         (s1[max_index, 1] - s1[i, 1]) ** 2)
    #     rroc = np.math.sqrt((s2[min_index, 0] - s1[i, 0]) ** 2 +
    #                         (s2[min_index, 1] - s1[i, 1]) ** 2)
    #     if rroj < rroc and rroj <= min_val:
    #         a = s1[i, :].reshape((1, 2))
    #         u = np.concatenate((u, a))
    s1 = np.setdiff1d(s1, u)
    s1 = s1.reshape((int(s1.shape[0] / 2)), 2)
    print(s1, '\n', np.size(s1, 0))
    # пока выборка не закончена,повторяем алгоритм
    while np.size(s1) != 0:
        distance, summary_dist = calc_dist(np.size(s1, 0), n2, s1, s2)
        max_val, max_index, min_val, min_index = find_min_max(distance, summary_dist)
        u2 = create_array_etalon(n1=np.size(s1, 0), s1=s1, s2=s2, max_index=max_index,
                                 min_index=min_index, min_val=min_val)

        for row in range(0, np.size(u, 0) - np.size(u2, 0)):
            u2 = np.vstack((u2, [0, 0]))
        u_end = np.concatenate((u, u2), axis=1)
        u = u_end
        s1 = np.setdiff1d(s1, u_end)
        s1 = s1.reshape((int(s1.shape[0] / 2)), 2)
        print('=========')
        print(s1, '\n', np.size(s1))
    return u


def calc_dist(n1, n2, s1, s2):
    distance = np.zeros(shape=(n1, n2))
    summary_dist = np.zeros(shape=(n1, 1))
    for i in range(0, n1):
        for j in range(0, n2):
            distance[i, j] = np.math.sqrt((s1[i, 0] - s2[j, 0]) ** 2 +
                                          (s1[i, 1] - s2[j, 1]) ** 2)
        summary_dist[i] = sum(distance[i])
    return distance, summary_dist


def find_min_max(distance, summary_distance):
    max_val = np.amax(summary_distance)  # центр 1-го эталона класса
    max_index = np.argmax(summary_distance)
    min_val = np.amin(distance[max_index, :])  # центр конкурирующего
    min_index = np.argmin(distance[max_index, :])
    return max_val, max_index, min_val, min_index


def create_array_etalon(n1, s1, s2, max_index, min_index, min_val):
    u = np.zeros([1, 2])
    for i in range(0, n1):
        rroj = np.math.sqrt((s1[max_index, 0] - s1[i, 0]) ** 2 +
                            (s1[max_index, 1] - s1[i, 1]) ** 2)
        rroc = np.math.sqrt((s2[min_index, 0] - s1[i, 0]) ** 2 +
                            (s2[min_index, 1] - s1[i, 1]) ** 2)
        if rroj < rroc and rroj <= min_val:
            a = s1[i, :].reshape((1, 2))
            u = np.concatenate((u, a))
    return u
