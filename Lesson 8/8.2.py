class DivExcept:

    def __init__(self, a, b):

        self.a = a

        self.b = b

    @property
    def division(self):

        try:

            return f'a/b = {round(self.a / self.b, 2)}'

        except ZeroDivisionError:

            return f'\nError! Division by zero.'
        # except ValueError:


anum = DivExcept(float(input('a = ')), float(input('b = ')))

print(anum.division)
