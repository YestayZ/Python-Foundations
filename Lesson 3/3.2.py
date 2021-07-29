def parameters(name, surname, birthyear, residence, email, tel):
    """Возвращает список словарей с данными о пользователе"""
    items = [name, surname, birthyear, residence, email, tel]
    keys = ['Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'email', 'телефон']
    dictionary = dict(zip(keys, items))
    return result.append(dictionary)


users = int(input(f"\nОбщее количество пользователей:  "))
i = 0
result = []
while i <= users - 1:
    print()
    a = str(input(f"Введите имя {i + 1}-ого пользователя:  "))
    b = str(input(f"Введите фамилию {i + 1}-ого пользователя:  "))
    c = str(input(f"Введите год рождения {i + 1}-ого пользователя:  "))
    d = str(input(f"Введите город проживания {i + 1}-ого пользователя:  "))
    e = str(input(f"Введите электронную почту {i + 1}-ого пользователя  "))
    f = str(input(f"Введите номер телефона {i + 1}-ого пользователя:  "))
    parameters(name=a, surname=b, birthyear=c, residence=d, email=e, tel=f)
    i += 1
print()

for i in result:
    print(i)

