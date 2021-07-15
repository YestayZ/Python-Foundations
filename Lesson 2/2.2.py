my_list = input("Введите элементы списка через пробел:  ").split()

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f"Значениями обменялись элементы 1 и 2,3 и 4 и т.д.: {my_list}")