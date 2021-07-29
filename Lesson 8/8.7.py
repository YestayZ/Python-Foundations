class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = None

    def __add__(self, other):
        return f'a + b = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'a * b = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z1 = Complex(81, -21)
z2 = Complex(13, -84)
print(z1)
print(z1 + z2)
print(z1 * z2)
