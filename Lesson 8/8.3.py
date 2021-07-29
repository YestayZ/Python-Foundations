class NumException(ValueError):
    pass


my_list = []
while True:
    try:
        number = input("Please, enter number('stop' to exit): ")
        if number == 'stop':
            break
        if not number.isdigit():
            raise NumException(number)
        my_list.append(float(number))
    except NumException as el:
        print(f"\nError! '{el}' is not a number")
print(my_list)
