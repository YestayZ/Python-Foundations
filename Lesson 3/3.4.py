def power_of(x, y):
    """Возвращает возведение числа x в степень y."""
    if x >= 0:
        if y <= 0:
            if y.is_integer() is False:
                return print(f"\ny ('{y}') is not whole integer.")
            else:
                return print(f"\n--------------------\n{x}^({y}) = {x ** y}\n--------------------")
        else:
            return print(f"\ny ('{y}') should be a negative number.")
    else:
        return print(f"\nx ({x}) should be a positive number.")


number1 = float(input(f"\nPlease enter real positive number x =  "))
number2 = float(input(f"\nPlease enter negative integer y =  "))
power_of(number1, number2)
