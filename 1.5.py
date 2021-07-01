profit = float(input('Выручка фирмы:    '))
cost = float(input('Убыток фирмы:   '))

if profit > cost:
    print('')
    print(f'Фирма работает хорошо! Выручка больше издержек. Рентабельность выручки: {profit / cost:.2f}')
    print('')
    print('')
    workers = int(input('Численность сотрудников фирмы:    '))
    print(f'Прибыль фирмы в расчете на одного сотрудника:   {profit/ workers:.2f}')
elif profit == cost:
        print('')
        print('Фирма работает в ноль.')
else:
    print('')
    print('Фирма работает плохо.')

