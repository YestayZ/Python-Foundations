def sal():
    try:
        time_worked = float(input(f'\nВыработка в часах:   '))
        hourly_rate = int(input('Ставка в час:  '))
        bonus = int(input('Премия:  '))
        salary = time_worked * hourly_rate + bonus
        return salary
    except ValueError:
        return print('Error! Not a number.')


print(f'\nЗаработная плата сотрудника составила {sal()}')
