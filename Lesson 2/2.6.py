keys = ["Название", "Цена", "Количество", "Единица измерения"]
items = []
overall_items = int(input("Общее количество уникальных товаров:   "))

num = 1
result = []

while overall_items >= int(num):
    i = 0
    my_tuple = ()
    items = []
    while i <= int(len(keys) - 1):
        items.append(input(f"{keys[i]} {num}-ого товара: "))
        i += 1
    dictionary = dict(zip(keys, items))
    my_tuple = (num, dictionary)
    result.append(my_tuple)
    num += 1
    print()

print("Структура товаров:")
for el in result:
    print(el)

statistics = {}
analyze = []
name = []
price = []
quantity = []
uom = []

i = 1

while i <= overall_items:
    name.append(result[i - 1][1].pop(keys[0]))
    price.append(result[i - 1][1].pop(keys[1]))
    quantity.append(result[i - 1][1].pop(keys[2]))
    check = result[i - 1][1].pop(keys[3])
    not_in_list = check not in uom
    if not_in_list is True:
        uom.append(check)
    else:
        print()
    i += 1
    analyze = (name, price, quantity, uom)
    statistics = dict(zip(keys, analyze))
print()
print("Аналитика товаров:")
n = 0

for k, v in statistics.items():
    print(k, ":", v)


