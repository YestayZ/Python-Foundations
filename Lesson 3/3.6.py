def int_func(a):
    a = str(a).title()
    print(f"\n{a}")


b = input(f"\nВведите слово из маленьких латинских букв: ")
if len(b.split()) > 1:
    print(f"\nНужно вести только одно слово.")
    import sys
    sys.exit()
else:
    int_func(b)
c = str(input(f"\nВведите строку из слов, разделенных пробелом и состоящих из латинских букв в нижнем регистре:  "))
int_func(c)