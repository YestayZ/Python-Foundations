def divide(a, b):
    """Возвращает деление а на b."""
    if b == 0:
        return print(f"\nError! Division by zero.")
    elif a % b == 0:
        return print("\na / b = %.f" % (a / b))

    else:
        return print(f'\n{a / b}')



int1 = list(input(f'\nPlease, enter number a:  '))
int2 = list(input(f'Please, enter number b:  '))

if len(int1) + len(int2) > 2:
    print(f"\nError! Wrong value(s) entered.")
    import sys
    sys.exit()
int1 = float(int1.pop())
int2 = float(int2.pop())
divide(a=int1, b=int2)
