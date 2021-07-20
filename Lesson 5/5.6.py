class_names = []
values = []
result = []
with open("text_hw56.txt", "r", encoding="utf-8") as file_obj:
    for items in file_obj:
        row = str(items).replace(":", "").replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").split()
        class_names.append(row[0])
        values.append(row[1:])
    for el in values:
        result.append(sum(map(int, el)))
    dictionary = dict(zip(class_names, result))
print(f'Dictionary: {dictionary}')
