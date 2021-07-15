try:
    with open("text_hw55.txt", "w+") as f_obj:
        numbers = input("Please, enter numbers separated by space: ")
        f_obj.writelines(numbers)
        numbers = numbers.split()
        sum_of = sum(map(int, numbers))
        print(f'The sum of numbers:  {sum_of}')
except ValueError:
    print("Error! wrong values entered.")