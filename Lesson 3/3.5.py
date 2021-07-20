def listsum(numList):
    """Возвращает сумму элементов списка."""
    total = list()
    if len(numList) == 1:
        return numList[0]
    else:
        return sum(numList)


def defining(a):
    """Проверяет на наличие специального символа, выводит ошибку в случае элемент не является цифрой,
       Возвращает сообщение и сумму элементов списка."""
    sum_of_numbers = list()  # суммирование вне цикла
    sum_in_iter = list() #суммирование в цикле в виде листа где последний элемент будет равен сумме
    n = 0
    for i in a:
        if i == "x": #специальный символ = 'x'
            if float(sum(sum_in_iter)) == 0: # если в списке нет символов кроме специального,
                print(f'\nProgram finished. Sum of elements = {listsum(sum_of_numbers) }') #не учитывается
            else:                                                                          #суммирование в цикле
                print(f'\nProgram finished. Sum of elements = {listsum(sum_of_numbers) + float(sum_in_iter.pop())}')
            import sys
            sys.exit()
        elif i.isdigit():
            n = float(i) + n
            sum_in_iter.append(n)
        else:
            print(f'\nYou entered wrong value - "{i}"')
    sum_of_numbers.append(n)
    int_sum = listsum(sum_of_numbers)
    return print(f"\nSum of elements = {int_sum}.To exit program use symbol 'x'.")




while True: #Создаем бесконечный цикл до того пока команды из функции не выключат программу.
    print('--------------------------------------')
    b = list(str(input(f"\nPlease, enter a list of numbers dividing by space: ")).split(" "))
    defining(b)






