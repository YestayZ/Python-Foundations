import json
companies = []
profits = []
m = []
with open("text_hw57.txt", "r") as f_obj:
    for items in f_obj:
        lists = items.split()
        companies.append(lists[0])
        profits.append(int(lists[2])-int(lists[3]))
dictionary = dict(zip(companies, profits))
for el in profits:
    if el > 0:
        m.append(el)
mid = sum(map(int, m)) / len(m)
middle = dict(Average_profit = int(mid))
result = []
result.append(dictionary)
result.append(middle)
with open("hw_57.json", "w") as write_f:
    json.dump(result, write_f)
