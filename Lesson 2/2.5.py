my_list = [10, 9, 9, 8, 7, 6, 5, 5,  2, 2, 1, 1]
print()
print(f"The initial list:   {my_list}")
print()
new = int(input("Please, enter next integer element in the list:    "))

result = []
i = 0
while i < len(my_list):

    if int(new) == int(my_list[i]):
        if int(i) == int(len(my_list)-1):
            result.append(my_list[i])
            result.append(new)
            i += 1
        else:
            if int(my_list[i]) == int(my_list[i+1]):
                n_times = my_list.count(my_list[i])
                from itertools import repeat
                result.extend(repeat(my_list[i], n_times))
                i += n_times
            else:
                result.append(my_list[i])
                i += 1
    else:
        not_in_list = new not in result
        if not_in_list is True:
            result.append(new)
            result.append(my_list[i])
            i += 1
        else:
            result.append(my_list[i])
            i += 1

result.sort(reverse=True)
print()
print(f"The final list:    {result}")