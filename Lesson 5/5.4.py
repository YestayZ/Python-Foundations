a = [x.split() for x in open("text_hw54.txt", "r") if x.rstrip()]
list_required = [' '.join(map(str, el)) for el in a]
list_required = [str(el).replace("One", "Один")
                     .replace("Two", "Два")
                     .replace("Three", "Три")
                     .replace("Four", "Четыре")
                     .replace("â€”", "–") for el in list_required]
with open("result_hw54.txt", "w", encoding="utf-8") as f_obj_in:
    for items in list_required:
        f_obj_in.write(items + '\n')