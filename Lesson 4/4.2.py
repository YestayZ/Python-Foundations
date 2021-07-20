my_list = [6, 3, 5, 0, 6, 4, 89, 234, 75, 21, 4, 6, 3, 2, 59]
new = [el for num, el in zip(my_list, my_list[1:]) if el > num]
print(f'Initial list = {my_list}\nFinal list = {new}')
