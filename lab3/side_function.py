import numpy as np


def flatten(iterable, types_to_flatten=(list, tuple)):
    flat_list = []
    for sublist in iterable:
        for items in sublist:
            flat_list.append(items)
    return flat_list


def uniq(array):
    a = flatten(array)
    a = np.unique(a)
    return a
