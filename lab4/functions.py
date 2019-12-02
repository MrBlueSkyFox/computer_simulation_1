import numpy as np
import copy


def prepare_etalon(S1, S2, n1, n2):
    # distance = np.zeros(shape=(n1, n2))
    # summary_dist = np.zeros(shape=(n1, 1))
    # for i in range(0, n1):
    #     for j in range(0, n2):
    #         distance[i, j] = np.math.sqrt((s1[i, 0] - s2[j, 0]) ** 2 +
    #                                       (s1[i, 1] - s2[j, 1]) ** 2)
    #     summary_dist[i] = sum(distance[i])
    s1 = copy.deepcopy(S1)
    s2 = copy.deepcopy(S2)
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
    # print(s1, '\n', np.size(s1, 0))
    # пока выборка не закончена,повторяем алгоритм
    # np.size(array, 0-rows ,1 -collumn)
    while np.size(s1) != 0:
        distance, summary_dist = calc_dist(np.size(s1, 0), n2, s1, s2)
        max_val, max_index, min_val, min_index = find_min_max(distance, summary_dist)
        u2 = create_array_etalon(n1=np.size(s1, 0), s1=s1, s2=s2, max_index=max_index,
                                 min_index=min_index, min_val=min_val)

        for row in range(0, np.size(u, 0) - np.size(u2, 0)):
            u2 = np.vstack((u2, [0, 0]))
        if u2.shape[1] !=2:
            print("SHIT")
        u_end = np.concatenate((u, u2), axis=1)
        u = u_end
        s1 = np.setdiff1d(s1, u_end)
        s1 = s1.reshape((int(s1.shape[0] / 2)), 2)
        # print('=========')
        # print(s1, '\n', np.size(s1))
    u = np.delete(u, 0, 0)
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


def etalon(u):
    leng = 0
    l = []
    for i in range(0, np.size(u, 1), 2):
        for j in range(0, np.size(u, 0)):
            if u[j, i] != 0.0 and u[j, i] != 0.0:
                leng = leng + 1
        l = np.append(l, leng)
        leng = 0
    x0 = []
    y0 = []
    for i in range(0, np.size(u, 1), 2):
        x0 = np.append(x0, np.sum(u[:, i] / l[int(i / 2 + 0.5)]))
        y0 = np.append(y0, np.sum(u[:, i + 1] / l[int(i / 2 + 0.5)]))
    return x0, y0, l


def control_element(M, Sig, z):
    c_e = []
    while np.size(c_e) != z:
        c = M + Sig * np.random.randn(1, 1)
        c_e = np.append(c_e, c)
    return c_e


def clean_etalon(L, X, Y):
    index_list = []
    i = 0
    for v in L:
        if v == 0 or v == 0.0:
            index_list.append(i)
        i += 1
    l = np.delete(L, index_list)
    x = np.delete(X, index_list)
    y = np.delete(Y, index_list)
    return l, x, y


def FRis_function(X01, Y01, X02, Y02, c_x, c_y, disp_1, disp_2):
    control_res1 = []
    control_res2 = []
    for i in range(0, X01.shape[0]):
        val_1 = np.math.sqrt(
            (X01[i] - c_x) ** 2 + (Y01[i] - c_y) ** 2
        )
        control_res1 = np.append(control_res1, val_1)
    for j in range(0, X02.shape[0]):
        val_2 = np.math.sqrt(
            (X02[j] - c_x) ** 2 + (Y02[j] - c_y) ** 2
        )
        control_res2 = np.append(control_res2, val_2)
    min_c1 = np.amin(control_res1)
    min_c2 = np.amin(control_res2)
    # сходство С1 с А в конкуренции с В
    # factor_f_1 = (min_c2 - min_c1) / (min_c2 - min_c1)
    factor_f_1 = (min_c2 * disp_1 - min_c1 * disp_2) / (min_c2 * disp_2 - min_c1 * disp_1)
    # сходство С1 с B  в конкуренции с А
    # factor_f_2 = (min_c1 - min_c2) / (min_c1 - min_c2)
    factor_f_2 = (min_c1 * disp_2 - min_c2 * disp_1) / (min_c1 * disp_2 - min_c2 * disp_1)

    if factor_f_1 > 0:
        return 1
    if factor_f_2 > 0:
        return 2
