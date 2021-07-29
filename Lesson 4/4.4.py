my_list = [2, 4, 5, 8, 3, 4, 1, 6, 2, 1, 5]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(f'initial list: \n{my_list}')
print(f'\nfinal list without duplications: \n{new_list}')