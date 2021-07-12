from itertools import cycle
from itertools import count


# a)
def counter(start, end):
    for i in count(start):
        if i > end:
            break
        else:
            print(int(i))
    print()


# b)
def cycling(list_num, num_iter):
    x = 0  # Чтобы узнать количество итерации
    y = 0  # Чтобы печатать элементы списка. Если элементов не осталось - y обнуляется и прибавляется 1 на х
    iterator = cycle(list_num)
    while True:
        if num_iter < x + 1:
            break
        if len(list_num) == y + 1:
            x += 1
            y = 0
        else:
            y += 1
        yield next(iterator)


my_list = [0, 1, 2, 3, 4]
try:
    a = int(input(f'\nEnter starting number:  '))
    b = float(input('Enter ending number:  '))
    counter(a, b)
    iteration = int(input(f'\nThe list of numbers = {my_list}\nPlease, enter number of iteration:  '))
    print(f'\nList repeated {iteration} times: {list(cycling(my_list, iteration))}')
except ValueError:
    print('Error! Wrong value entered.')
    exit(1)
