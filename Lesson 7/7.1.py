import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        data_set = np.array(self.data)
        return print('\n'.join(map(str, data_set)))

    def __add__(self, other):
        result = []
        for i in range(len(self.data)):
            result.append([])
            for j in range(len(self.data[i])):
                result[i].append(self.data[i][j] + other.data[i][j])
        return '\n'.join(map(str, result))


numbers = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
numbers_2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
numbers.__str__()
print(f'\n {numbers + numbers_2}')
