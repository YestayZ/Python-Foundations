# try:
#     f_obj = open("test.txt")
#     for line in f_obj:
#         print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
    # f_obj.close()



try:
    with open("test.txt") as f_obj:
        for line in f_obj:
            print(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")

    
f_obj = open("test.txt")
print(f_obj.read(3))
print("Мы находимся на позиции: ", f_obj.tell())
# Перемещаемся в начало
f_obj.seek(0)
print(f_obj.read(10))
f_obj.close()