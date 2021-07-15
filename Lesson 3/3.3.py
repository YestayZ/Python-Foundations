def my_func(a, b, c):
    """Возвращает сообщение и сумму наибольших двух аргументов."""
    if a < b:
        minimum = a
    else:
        minimum = b
    if c < minimum:
        minimum = c
    s = a + b + c - minimum
    print(f"\nSum of the two biggest numbers = {s}")

print()
num1 = int(input("Enter number a = "))
num2 = int(input("Enter number b = "))
num3 = int(input("Enter number c = "))
my_func(num1,num2,num3)
