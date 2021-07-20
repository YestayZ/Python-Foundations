print('')
m_num = input('Введите месяц в виде целого цисла от 1 до 12:   ')
num_check = m_num.isnumeric()
if num_check is True:
    m_num = int(m_num)
    if 0 < m_num < 13:
        print('')
    else:
        print('')
        print("Извините, нет такого месяца года.")
        import sys
        sys.exit()
else:
    print('')
    print("Извините, нет такого месяца года.")
    import sys
    sys.exit()

seasons = ['Весна', 'Лето', 'Осень', 'Зима']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


i = 1
d = {}
list = []

while 0 < i < 13:
    if 1 == i:
        d = {numbers[i - 1]: seasons[3]}
        list.append(d)
    elif 2 < i < 6:
        d = {numbers[i - 1]: seasons[0]}
        list.append(d)
    elif 5 < i < 9:
        d = {numbers[i - 1]: seasons[1]}
        list.append(d)
    elif 8 < i < 12:
        d = {numbers[i - 1]: seasons[2]}
        list.append(d)
    else:
        d = {numbers[i - 1]: seasons[3]}
        list.append(d)

    if m_num == i:
        result = list[i-1]
        print(f"В {m_num}-ом месяце на улице будет {result.pop(i)}.")
    i += 1
