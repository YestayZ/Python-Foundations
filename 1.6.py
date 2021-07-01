first_day = float(input('Результат первого дня пробежки в км: a - '))
last_day = float(input('Результат спортсмена в километрах: b - '))

i=1
while last_day - first_day >= 0:
    first_day = first_day +(first_day * 0.1)
    i += 1
print(f'День, когда спортсмен достиг результата {last_day:.2f} км: ', i)

