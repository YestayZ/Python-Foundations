from math import factorial


def fact(number):
    for i in range(1, number + 1):
        yield factorial(i)


n = int(input(f'\nPlease, enter number:  '))

for el in fact(n):
    print(el)
