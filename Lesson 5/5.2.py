my_list = [len(x.rstrip().split()) for x in open("text_hw52.txt", "r") if x.rstrip()]
print(f'\nКоличество строк в файле: {len(my_list)}\n')
i = 1
for items in my_list:
    print(f'Количество слов в {i}-ой строке - {items} ')
    i += 1
