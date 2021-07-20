from functools import reduce


def multiple(i, i_prev):
    return i * i_prev


num_list = [el for el in range(100, 1001, 2)]
print(reduce(multiple, num_list))
